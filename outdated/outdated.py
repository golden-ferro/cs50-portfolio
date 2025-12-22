m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").strip()
        if date[0].isnumeric():
            month, day, year = date.split("/")
            month = int(month.strip())
            day = int(day.strip())
            year = int(year.strip())
            if month > 12 or day >31:
                raise ValueError
            print(f"{year}-{month:02}-{day:02}")
        if date[0].isalpha():
            x, year = date.split(",")
            month, day = x.split(" ")
            month = month.strip()
            day = int(day.strip())
            year = int(year.strip())
            if (m.index(month) + 1) > 12 or day >31:
                raise ValueError
            print(f"{year}-{((m.index(month)) + 1):02}-{day:02}")
        break
    except ValueError:
        continue
