from database import database
from CreateAccount import UserRegistration
from Balance import Balance
from MoneyTransfer import transaction
from AccountDetails import users_details
from loancalculator import balance
from AccountHistory import *


def final():
    while True:
        try:
            print("1: Create Account")
            print("2: Add Funds")
            print("3: Money Transfer")
            print("4: User Details")
            print("5: Loan Calculation")
            print("6: Account History")
            print("7: Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                UserRegistration().register_user()
            elif choice == 2:
                Balance().top_up_balance()
            elif choice == 3:
                sender_account = input("Enter Your Account Number: ")
                receiver_account = input("Enter The Account Number Of The Receiver: ")
                amount = float(input("Enter The Amount Of Money: "))
                transaction(sender_account, receiver_account, amount)
            elif choice == 4:
                account_number = input("Enter Your Account Number: ")
                users_details(account_number, database)
            elif choice == 5:
                balance(database)
            elif choice == 6:
                account_number = input("Enter account number: ")
                if account_number in history:
                    print("Transaction history for account:", account_number)
                    for transaction_detail in history[account_number]:
                        print("-", transaction_detail)
            elif choice == 7:
                print("Exiting...")
                break 
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    final()
