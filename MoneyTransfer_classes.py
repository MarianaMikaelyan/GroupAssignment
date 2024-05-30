import csv
from datetime import datetime
from CreateAccount import database
from AccountHistory import save_transaction 

class Transaction:
    def __init__(self, sender_account, receiver_account, amount):
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.amount = amount

    def execute(self):
        if self.sender_account in database and self.receiver_account in database:
            if database[self.sender_account]['Balance'] >= self.amount:
                database[self.sender_account]['Balance'] -= self.amount
                database[self.receiver_account]['Balance'] += self.amount
                transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Transaction successful! {self.amount} GEL transferred from {self.sender_account} to {self.receiver_account} at {transaction_time}.")
                save_transaction(self.sender_account, f"Sent: -{self.amount} GEL to {self.receiver_account} at {transaction_time}")
                save_transaction(self.receiver_account, f"Received: +{self.amount} GEL from {self.sender_account} at {transaction_time}")
                self.log_transaction(self.sender_account, database[self.sender_account]['First Name'], database[self.sender_account]['Last Name'], "Sent", transaction_time)
                self.log_transaction(self.receiver_account, database[self.receiver_account]['First Name'], database[self.receiver_account]['Last Name'], "Received", transaction_time)
            else:
                print("Insufficient balance.")
                save_transaction(self.sender_account, f"Failed to send: -{self.amount} GEL to {self.receiver_account}")
        else:
            print("Invalid account number(s).")

    @staticmethod
    def log_transaction(account_number, first_name, last_name, transaction_type, transaction_time):
        with open("transactions.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, account_number, amount, transaction_type, transaction_time])

        with open("transactions.txt", "a") as file:
            file.write(f"{first_name}, {last_name}, {account_number}, {amount}, {transaction_type}, {transaction_time}\n")

if __name__ == "__main__":
    sender_account_number = input("Enter Your Account Number: ")
    receiver_account_number = input("Enter The Account Number Of The Receiver: ")
    amount = float(input("Enter The Amount Of Money: "))

    transaction = Transaction(sender_account_number, receiver_account_number, amount)
    transaction.execute()
