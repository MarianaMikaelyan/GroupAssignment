from database import database

class UserDetails:
    @staticmethod
    def display(account_number, database):
        if account_number.strip() != "":
            if account_number in database:
                user_details = database[account_number]
                print("First Name:", user_details['First Name'])
                print("Last Name:", user_details['Last Name'])
                print("Balance:", user_details['Balance'])
            else:
                print("User Not Found")
        else:
            print("Please enter a non-empty account number.")

if __name__ == "__main__":
    account_number = input("Enter Your Account Number: ")
    UserDetails.display(account_number, database)
