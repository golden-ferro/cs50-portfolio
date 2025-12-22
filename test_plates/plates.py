import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if any(ch.isalpha() for ch in s[i:]):
                return False
            break

    for ch in s:
        if not ch.isalnum():
            return False

    return True


if __name__ == "__main__":
    main()
