from database import database

def add_funds(account_number, amount, accounts):
    account_number = input("Enter your account number: ")
    top_up_amount = float(input("Enter the amount to top up: "))
    add_funds(account_number, top_up_amount, database)
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


if __name__ == "__main__":
    add_funds()