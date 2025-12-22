def main():
    word = input("Input: ")
    print("Output: ", end="")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = ""
    for c in word:
        if c not in vowels:
            output = output + c
    return output

if __name__ == "__main__":
    main()
