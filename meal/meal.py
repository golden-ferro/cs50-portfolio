def main():
    time = input("What time is it? ").strip()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m)
    m = m/60
    return m + h

if __name__ == "__main__":
    main()
