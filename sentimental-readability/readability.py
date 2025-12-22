def count_letter(text):
    counter = 0
    for char in text:
        if char.isalpha():
            counter += 1
    return counter

def count_word(text):
    counter = 1
    for char in text:
        if char.isspace():
            counter += 1
    return counter

def count_sentence(text):
    counter = 0
    punctuation = ".!?"
    for char in text:
        if char in punctuation:
            counter += 1
    return counter

def main():
    text = input("text: ")

    L = count_letter(text) / count_word(text) * 100
    S = count_sentence(text) / count_word(text) * 100

    index = 0.0588 * L - 0.296 * S - 15.8
    index = round(index)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade , {index}")
main()
