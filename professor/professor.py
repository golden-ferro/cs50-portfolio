import random

def main():
    c = 1
    points = 0

    level = get_level()

    while c <= 10:
        mistakes = 0
        a = generate_integer(level)
        b = generate_integer(level)
        x = a + b

        while mistakes < 3:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == x:
                    points += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
            except ValueError:
                print("EEE")
                mistakes += 1

        if mistakes == 3:
            print(f"{a} + {b} = {x}")

        c += 1

    print(f"Score: {points}")


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
