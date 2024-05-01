from database import database

history = []

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

def balance1():
    global history
    account_number = input("Enter your account number: ")
    top_up_amount = input("Enter the amount to top up: ")

    try:
        top_up_amount = float(top_up_amount)
        transaction_info = add_funds(account_number, top_up_amount, database)  # Removed colon here
        if transaction_info:
            history.append(transaction_info)

    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")

if __name__ == "__main__":
    balance1()
