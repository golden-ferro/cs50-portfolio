from validator_collection import validators, errors

def main():
    email = input("Email: ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

def is_valid_email(email):
    try:
        validators.email(email) 
        return True
    except errors.InvalidEmailError:
        return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()
