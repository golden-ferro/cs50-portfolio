user = 0
due = 50
while user < 50:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin != 25 and coin != 10 and coin != 5:
        continue
    user = user + coin
    due = due - coin
print(f"Change Owed: {user - 50}")
