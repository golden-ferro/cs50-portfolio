expression = input("Expression: ").strip()
a, operator, b = expression.split(" ")
a = float(a)
b = float(b)

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b

print(f"{result:.1f}")


