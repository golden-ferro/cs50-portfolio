import sys
import random

while True:
    try:
        level = int(input("level: "))
        if level >= 1:
            break
    except ValueError:
        print("Please enter a valid number!")
        continue

n = random.randint(1, level)

while True:
    try:
        guess = int(input("guess: "))
        if guess < 1:
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue
    if guess < n:
        print("Too small!")
        continue
    if guess > n:
        print("Too large!")
        continue
    if guess == n:
         print("Just right!")
         sys.exit()



