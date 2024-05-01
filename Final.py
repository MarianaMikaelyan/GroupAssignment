#საბოლოო

from database import database
from createaccount import register_user
from balance import balance1
from MoneyTransfer import transaction
from accountdetails import users_details
from loancalculator import balance
from accounthistory import history_all

def final():
    while True:
        try:
            choice  = int(input("Enter your choice (1: CreateAccount, 2: Add_funds, 3: MoneyTransfer, 4: Users Details, 5: Loan Calculation, 6: history_all, 7: Exit): "))
    
            if choice == 1:
                register_user()
            elif choice == 2:
                balance1()
            elif choice == 3:
                sender_account = input("Enter Your Account Number: ")
                receiver_account = input("Enter The Account Number Of The Receiver: ")
                amount = float(input("Enter The Amount Of Money: "))
                transaction(sender_account, receiver_account, amount, database)
            elif choice == 4:
                account_number = input("Enter Your Account Number: ")
                users_details(account_number, database)
            elif choice == 5:
               balance(database)
            elif choice == 6:
               history_all()
            elif choice == 7:
                break 
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    final()
