<<<<<<< HEAD
from createaccount import database
=======
from CreateAccount import database
import datetime
>>>>>>> 0809baa4f42e2e96256eacab529e036bd5dd567a

def transaction(sender_account, receiver_account, amount, accounts):
    if sender_account in accounts:
        if receiver_account in accounts:
            if amount <= accounts[sender_account]['Balance']:
                accounts[sender_account]['Balance'] -= amount
                accounts[receiver_account]['Balance'] += amount
<<<<<<< HEAD
=======
                database[sender_account]['History'].append({'Timestamp': datetime.datetime.now(), 'Type': 'Transaction', 'Sender Account': sender_account, 'Receiver Account': receiver_account, 'Amount': amount})
                database[receiver_account]['History'].append({'Timestamp': datetime.datetime.now(), 'Type': 'Transaction', 'Sender Account': sender_account, 'Receiver Account': receiver_account, 'Amount': amount})
>>>>>>> 0809baa4f42e2e96256eacab529e036bd5dd567a
                print("The transaction was completed successfully.", 
                      accounts[sender_account]['First Name'], "-->", 
                      accounts[receiver_account]['First Name'], ":", amount)
            else:
                print("Not Enough Money")
        else:
            print("Receiver Not Found")
    else:
        print("User Not Found")

<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == "_main_":
>>>>>>> 0809baa4f42e2e96256eacab529e036bd5dd567a
    sender_account = input("Enter Your Account Number: ")
    receiver_account = input("Enter The Account Number Of The Receiver: ")
    amount = float(input("Enter The Amount Of Money: "))

    transaction(sender_account, receiver_account, amount, database)