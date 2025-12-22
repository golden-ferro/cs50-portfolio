def main():
    name = input("camelCase: ")

    print(camelCase(name))

def camelCase(name):
    c = ""
    for i in name:
        if i.isupper():
            c = c + "_" + i.lower()
        else:
            c = c + i
    return c
main()
