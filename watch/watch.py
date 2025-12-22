import re

def main():
    s = input("HTML: ")
    print(parse(s))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"'
    match = re.search(pattern, s)
    if match:
        return "https://youtu.be/" + match.group(1)
    else:
        return "None"


if __name__ == "__main__":
    main()
