entry = input("height between 1 and 8: ")
while not entry.isdigit() or int(entry) < 1 or int(entry) > 8:
    entry = (input("height between 1 and 8: "))
    
height = int(entry)
for i in range(height):
    print((height - (i + 1)) * " ", end="")
    print((i + 1) * "#", end="")
    print(2 * " ", end="")
    print((i + 1) * "#")
