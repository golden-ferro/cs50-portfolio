import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    if len(s) >6:
        return False
    if len(s) <2:
        return False
    for c in range(len(s)):
        if s[c].isdigit():
            if s[c] == "0":
                return False
            for i in range(c, len(s)):
                if s[i].isalpha():
                    return False
            break
    for j in s:
        if j in string.punctuation:
            return False
    return True
main()
