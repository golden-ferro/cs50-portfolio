from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input("input: ")
    print(figlet.renderText(text))

main()

