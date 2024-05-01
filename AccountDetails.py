from createaccount import database


def users_details(account_number, accounts):
    if account_number in accounts:
        user_details = accounts[account_number]
        print( "First Name: ",user_details['First Name'],"Last Name: ",user_details['Last Name'],"Balance", user_details['Balance'])
    else:
        print("User Not Found")
        
if __name__ == "__main__":
    account_number = input("Enter Your Account Number: ")
    users_details(account_number, database)



