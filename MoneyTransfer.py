from createaccount import database

def transaction(sender_account, receiver_account, amount, accounts):
    if sender_account in accounts:
        if receiver_account in accounts:
            if amount <= accounts[sender_account]['Balance']:
                accounts[sender_account]['Balance'] -= amount
                accounts[receiver_account]['Balance'] += amount
                print("The transaction was completed successfully.", 
                      accounts[sender_account]['First Name'], "-->", 
                      accounts[receiver_account]['First Name'], ":", amount)
            else:
                print("Not Enough Money")
        else:
            print("Receiver Not Found")
    else:
        print("User Not Found")

if __name__ == "__main__":
    sender_account = input("Enter Your Account Number: ")
    receiver_account = input("Enter The Account Number Of The Receiver: ")
    amount = float(input("Enter The Amount Of Money: "))

    # Call the transaction function
    transaction(sender_account, receiver_account, amount, database)