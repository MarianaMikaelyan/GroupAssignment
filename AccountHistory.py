<<<<<<< HEAD
from balance import history
def history_all():
        print(history)
if __name__ == "__main__":
    history_all()
=======
#ანგარიშის ისტორია:

#შეინახეთ და აჩვენეთ მომხარებელს მისი ისტორია, ისტორიაში უნდა ინახებოდეს როგორც გადარიცხვები ასევე ბალანსზე შეტანის ისტორია
# ( დაუბეჭდეთ მხოლოდ თავისი ანგარიშის ისტორია )
#დაამატეთ ფილტრაცია, მომხარებელს შეეძლოს მხოლოდ ბალანსის შევსების ნახვა ან მხოლოდ გადარიცხვების ნახვა

import datetime
from AccountHistory import database

history = []

def filter_history(account_number, transaction_type):
    if account_number in database:
        user_history = database[account_number]['History']
        filtered_history = [i for i in user_history if i['Type'] == transaction_type]
        for i in filtered_history:
            print(i)
    else:
        print("User Not Found")

account_number = input("Enter your account number: ")
transaction_type = input("Enter transaction type (Deposit/Transaction): ")

filter_history(account_number, transaction_type)

>>>>>>> 0809baa4f42e2e96256eacab529e036bd5dd567a
