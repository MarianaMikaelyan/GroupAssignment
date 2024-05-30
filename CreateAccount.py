import csv
import random
import string
from database import database


class UserRegistration:
    def __init__(self):
        self.account_number = self.validate_account_number()
        self.user_id = self.generate_user_id()

    @staticmethod
    def validate_account_number():
        prefix = 'TB'
        digits = ''.join(random.choice(string.digits) for _ in range(4))
        account_number = prefix + digits
        return account_number

    @staticmethod
    def generate_user_id():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def register_user(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        initial_balance = float(input("Enter initial balance (not more than 100 GEL): "))

        if initial_balance <= 100:
            new_account_number = self.account_number
            user_id = self.user_id
            database[new_account_number] = {'First Name': first_name, 'Last Name': last_name,
                                            'Balance': initial_balance}

            with open('users.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, first_name, last_name, new_account_number, initial_balance])

            print("You have registered successfully.")
            print("Your new account number is:", new_account_number)

        else:
            print("Initial balance cannot exceed 100 GEL.")