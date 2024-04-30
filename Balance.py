from database import *



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


if __name__ == "__main__":
    add_funds()
