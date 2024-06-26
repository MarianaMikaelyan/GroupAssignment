from database import database
from AccountHistory import save_transaction




class Balance:
    @staticmethod
    def add_funds(amount):
        account_number = input("Enter your account number: ")
        if account_number in database:
            if isinstance(amount, (int, float)) and amount > 0:
                database[account_number]['Balance'] += amount
                print(
                    f"Balance was filled with {amount} GEL. New balance: {database[account_number]['Balance']} GEL")
                save_transaction(account_number, f"Top up: +{amount} GEL")
                return True
            else:
                print("Invalid amount entered. Please enter a positive number.")
        else:
            print("Invalid account number. Please enter a valid account number.")
        return False

    def top_up_balance(self):
        top_up_amount = input("Enter the amount to top up: ")
        try:
            top_up_amount = float(top_up_amount)
            success = self.add_funds(top_up_amount)
            if success:
                print("Transaction successful.")
            else:
                print("Transaction failed.")
        except ValueError:
            print("Invalid amount entered. Please enter a valid number.")
