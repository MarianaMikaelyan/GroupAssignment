import random
import string

database = {}
__all__ = ['database']

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


register_user()


def add_funds(account_number, amount, accounts):
    if account_number in accounts:
        if isinstance(amount, (int, float)) and amount > 0:
            accounts[account_number]['Balance'] += amount
            print(f"Balance was filled with {amount} GEL. New balance: {accounts[account_number]['Balance']} GEL")
            return True
        else:
            print("Invalid amount entered. Please enter a positive number.")
    else:
        print("Invalid account number. Please enter a valid account number.")
    return False


account_number = input("Enter your account number: ")
top_up_amount = float(input("Enter the amount to top up: "))

add_funds(account_number, top_up_amount, database)