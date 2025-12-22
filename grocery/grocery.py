grocery = {}
while True:
    try:
        item = input().upper().strip()
        if item in grocery:
            grocery[item] = grocery[item] + 1
        if item not in grocery:
            grocery[item] = 1
    except EOFError:
        print("\n")
        for key in sorted(grocery):
            print(grocery[key], key )
        break
