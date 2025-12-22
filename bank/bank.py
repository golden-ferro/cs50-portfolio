hello = input("Greeting: ")
hello = hello.strip().lower()

if hello[0:5] == "hello":
    print("$0")
elif hello[0] == "h":
    print("$20")
else:
    print("$100")
