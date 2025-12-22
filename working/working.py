import re

def main():
    h = input("Hours: ")
    print(convert(h))

def convert(s):
    pattern = r"(\d{1,2}):?(\d\d)? (AM|PM) to (\d{1,2}):?(\d\d)? (AM|PM)"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Input format is invalid")

    # f = first, s = second, n = new format, h = hour, m = minute

    fh = match.group(1)
    fm = match.group(2)
    fampm = match.group(3)
    sh = match.group(4)
    sm = match.group(5)
    sampm = match.group(6)

    fh = int(fh)
    if not (1 <= fh <= 12):
        raise ValueError("Hour value is invalid")
    nfh = (fh % 12) + (12 if fampm == "PM" else 0)

    nfm = int(fm) if fm is not None else 0
    if not (0 <= nfm < 60):
        raise ValueError("Minute value is invalid")

    sh = int(sh)
    if not (1 <= sh <= 12):
        raise ValueError("Hour value is invalid")
    nsh = (sh % 12) + (12 if sampm == "PM" else 0)

    nsm = int(sm) if sm is not None else 0
    if not (0 <= nsm < 60):
        raise ValueError("Minute value is invalid")

    return f"{nfh:02}:{nfm:02} to {nsh:02}:{nsm:02}"

if __name__=="__main__":
    main()

