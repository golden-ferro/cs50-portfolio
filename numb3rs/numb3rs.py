import re
import sys

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid")
    else:
        print("Invalid")


def validate(ip):
    c = 0
    pattern = r"([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)\.([1-9]\d{0,2}|0)"
    match = re.fullmatch(pattern, ip)
    if not match:
        return False

    for n in match.groups():
        n = int(n)
        if n >= 0 and n <= 255:
            c = c + 1

    if c == 4:
        return True
    else:
        return False

if __name__=="__main__":
    main()
