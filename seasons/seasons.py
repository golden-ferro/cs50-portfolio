from datetime import date
import sys
import inflect
import re

def main():
    birth_date = date_input()
    birth_date = date.fromisoformat(birth_date)
    today = date.today()

    days = (today - birth_date).days
    minutes = days * 24 * 60

    print(value_in_words(minutes))

def value_in_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes)
    words= words.replace(" and ", " ")
    return words.capitalize() + " minutes"

def date_input():
    birth_str = input("Date of Birth: ")
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
    match = re.match(pattern, birth_str)
    if match:
        return match.group()
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
