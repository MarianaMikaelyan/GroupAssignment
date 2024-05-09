import csv
from datetime import datetime
from CreateAccount import database
from AccountHistory import save_transaction 

def transaction(sender_account, receiver_account, amount):
    if sender_account in database and receiver_account in database:
        if database[sender_account]['Balance'] >= amount:
            database[sender_account]['Balance'] -= amount
            database[receiver_account]['Balance'] += amount
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Transaction successful! {amount} GEL transferred from {sender_account} to {receiver_account} at {transaction_time}.")
            save_transaction(sender_account, f"Sent: -{amount} GEL to {receiver_account} at {transaction_time}")
            save_transaction(receiver_account, f"Received: +{amount} GEL from {sender_account} at {transaction_time}")
            save_trans(sender_account, database[sender_account]['First Name'], database[sender_account]['Last Name'], amount, "Sent", transaction_time)
            save_trans(receiver_account, database[receiver_account]['First Name'], database[receiver_account]['Last Name'], amount, "Received", transaction_time)
        else:
            print("Insufficient balance.")
            save_transaction(sender_account, f"Failed to send: -{amount} GEL to {receiver_account}")
    else:
        print("Invalid account number(s).")

def save_trans(account_number, first_name, last_name, amount, transaction_type, transaction_time):
    with open("transactions.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, account_number, amount, transaction_type, transaction_time])

    with open("transactions.txt", "a") as file:
        file.write(f"{first_name}, {last_name}, {account_number}, {amount}, {transaction_type}, {transaction_time}\n")

if __name__ == "__main__":
    sender_account = input("Enter Your Account Number: ")
    receiver_account = input("Enter The Account Number Of The Receiver: ")
    amount = float(input("Enter The Amount Of Money: "))
    transaction(sender_account, receiver_account, amount)
