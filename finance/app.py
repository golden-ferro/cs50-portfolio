import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    rows = db.execute("""
        SELECT symbol, SUM(shares) as shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING SUM(shares) > 0
    """, user_id)

    holdings = []
    total_stocks_value = 0

    for row in rows:
        quote = lookup(row["symbol"])
        if not quote:
            continue

        price = float(quote["price"])
        total = price * row["shares"]

        holdings.append({
            "symbol": quote["symbol"],
            "name": quote["name"],
            "shares": row["shares"],
            "price": price,
            "total": total
        })
        total_stocks_value += total

    user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = float(user[0]["cash"])
    grand_total = cash + total_stocks_value

    return render_template("index.html", holdings=holdings, cash=cash, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")

    symbol = request.form.get("symbol")
    shares_str = request.form.get("shares")

    if not symbol:
        return apology("must provide symbol", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    # validate shares
    try:
        shares = int(shares_str)
        if shares <= 0:
            raise ValueError
    except:
        return apology("shares must be positive integer", 400)

    price = float(quote["price"])
    cost = price * shares

    user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = float(user[0]["cash"])

    if cash < cost:
        return apology("can't afford", 400)

    # transaction
    db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
               session["user_id"], quote["symbol"], shares, price)

    db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", cost, session["user_id"])

    flash("Bought!")
    return redirect("/")


@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]
    rows = db.execute("""
        SELECT symbol, shares, price, timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, user_id)

    history = []
    for r in rows:
        history.append({
            "action": "BUY" if r["shares"] > 0 else "SELL",
            "symbol": r["symbol"],
            "shares": abs(r["shares"]),
            "price": r["price"],
            "timestamp": r.get("timestamp", "")  # prevents KeyError
        })

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return apology("must provide username", 403)
        if not password:
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")

    symbol = request.form.get("symbol")

    if not symbol:
        return apology("must provide symbol", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    return render_template("quoted.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    if not username:
        return apology("must provide username", 400)
    if not password:
        return apology("must provide password", 400)
    if password != confirmation:
        return apology("passwords do not match", 400)

    user_exist = db.execute("SELECT id FROM users WHERE username = ?", username)
    if user_exist:
        return apology("username already exists", 400)

    hash_pass = generate_password_hash(password)

    new_user_id = db.execute(
        "INSERT INTO users (username, hash) VALUES (?, ?)",
        username, hash_pass
    )

    session["user_id"] = new_user_id
    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]

    if request.method == "GET":
        rows = db.execute("""
            SELECT symbol, SUM(shares) as shares
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, user_id)
        return render_template("sell.html", symbols=[r["symbol"] for r in rows])

    symbol = request.form.get("symbol")
    shares_str = request.form.get("shares")

    if not symbol:
        return apology("must select symbol", 400)

    try:
        shares = int(shares_str)
        if shares <= 0:
            raise ValueError
    except:
        return apology("shares must be positive integer", 400)

    row = db.execute("""
        SELECT SUM(shares) as shares
        FROM transactions
        WHERE user_id = ? AND symbol = ?
    """, user_id, symbol)

    owned = row[0]["shares"]
    if not owned or owned < shares:
        return apology("not enough shares", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    price = float(quote["price"])
    proceeds = price * shares

    db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
               user_id, symbol, -shares, price)

    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", proceeds, user_id)

    flash("Sold!")
    return redirect("/")

@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Allow user to add cash"""
    if request.method == "POST":
        try:
            amount = float(request.form.get("amount"))
        except ValueError:
            return apology("amount must be a number", 400)

        if amount <= 0:
            return apology("amount must be positive", 400)

        user_id = session["user_id"]

        # Atualiza o dinheiro do usuário
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, user_id)

        flash("Cash Added!")
        return redirect("/")

    else:
        return render_template("add.html")
