cardnum = input("Credit card number: ")
while not cardnum.isdigit():
    cardnum = input("Credit card number: ")

counter = 1
total = 0
length = len(cardnum)
cardnumres = int(cardnum)
cardnum_copy = int(cardnum)


while cardnum_copy > 0:
    remainder = cardnum_copy % 10
    cardnum_copy = cardnum_copy // 10

    if counter % 2 == 0:
        remainder *= 2
        if remainder > 9:
            remainder = (remainder % 10) + (remainder // 10)

    total += remainder
    counter += 1

if total % 10 == 0:
    start_digits = int(str(cardnumres)[:2])
    first_digit = int(str(cardnumres)[0])

    if (start_digits == 34 or start_digits == 37) and length == 15:
        print("AMEX")
    elif 51 <= start_digits <= 55 and length == 16:
        print("MASTERCARD")
    elif first_digit == 4 and length in [13, 16]:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
