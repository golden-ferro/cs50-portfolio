import re

def main():
    text = input("Text: ")
    print(count(text))

def count(s):
    s = s.lower()
    pattern = r"\bum\b[.,!?;:()\"']?"
    matches = re.findall(pattern, s)
    return len(matches)

if __name__=="__main__":
    main()
