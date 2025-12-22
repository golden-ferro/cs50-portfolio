while True:
    try:
        fuel = input("Fraction: ").strip()
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x>y or x<0 or y<0:
            raise ValueError
        p = (x / y) * 100
        if p >= 99:
            print("F")
        elif p <= 1:
            print("E")
        else:
            print(f"{p:.0f}%")
        break
    except (ValueError, ZeroDivisionError):
        print("invalid input")

