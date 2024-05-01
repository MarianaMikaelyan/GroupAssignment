from database import database
import datetime


def add_funds(account_number, amount, accounts):
    if account_number in accounts:
        if isinstance(amount, (int, float)) and amount > 0:
            accounts[account_number]['Balance'] += amount
            accounts[account_number]['History'].append({'Timestamp': datetime.datetime.now(), 'Type': 'Deposit', 'Amount': amount, 'Account Number': account_number})
            print(f"Balance was filled with {amount} GEL. New balance: {accounts[account_number]['Balance']} GEL")
            return True
        else:
            print("Invalid amount entered. Please enter a positive number.")
    else:
        print("Invalid account number. Please enter a valid account number.")
    return False

def balance():
    account_number = input("Enter your account number: ")
    top_up_amount = input("Enter the amount to top up: ")

    try:
        top_up_amount = float(top_up_amount)
        if add_funds(account_number, top_up_amount, database):
            # Update database or do further processing here
            pass
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")

if __name__ == "_main_":
    add_funds()