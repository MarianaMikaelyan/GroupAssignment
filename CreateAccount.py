import random
import string


from database import *


def validate_account_number():
    prefix = 'TB'
    digits = ''.join(random.choice(string.digits) for _ in range(4))
    account_number = prefix + digits
    return account_number


def register_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    initial_balance = float(input("Enter initial balance (not more than 100 GEL): "))

    if initial_balance <= 100:
        new_account_number = validate_account_number()  # Corrected variable name
        database[new_account_number] = {'First Name': first_name, 'Last Name': last_name, 'Balance': initial_balance}
        print("You have registered successfully.")
        print("Your new account number is:", new_account_number)
    else:
        print("Initial balance cannot exceed 100 GEL.")
        balance = 0


if __name__ == "__main__":
    register_user()