from CreateAccount import database
from AccountHistory import save_transaction 

def transaction(sender_account, receiver_account, amount):
    if sender_account in database and receiver_account in database:
        if database[sender_account]['Balance'] >= amount:
            database[sender_account]['Balance'] -= amount
            database[receiver_account]['Balance'] += amount
            print(f"Transaction successful! {amount} GEL transferred from {sender_account} to {receiver_account}.")
            save_transaction(sender_account, f"Sent: -{amount} GEL to {receiver_account}")
            save_transaction(receiver_account, f"Received: +{amount} GEL from {sender_account}")
        else:
            print("Insufficient balance.")
            save_transaction(sender_account, f"Failed to send: -{amount} GEL to {receiver_account}")
    else:
        print("Invalid account number(s).")

if __name__ == "__main__":
    sender_account = input("Enter Your Account Number: ")
    receiver_account = input("Enter The Account Number Of The Receiver: ")
    amount = float(input("Enter The Amount Of Money: "))
    transaction(sender_account, receiver_account, amount)
