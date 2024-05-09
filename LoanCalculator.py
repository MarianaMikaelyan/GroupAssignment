import csv
from datetime import datetime, timedelta
from database import database

def add_funds(account_number, loan_amount, loan_interest_rate, total_payable_amount, decision, accounts):
    if account_number in accounts:
        if decision == 1:
            accounts[account_number]['Balance'] += total_payable_amount
            print(f"Balance was filled with {total_payable_amount} GEL. New balance: {accounts[account_number]['Balance']} GEL")

            generate_loan_schedule(account_number, loan_amount, loan_interest_rate)

        if 'Loans' not in accounts[account_number]:
            accounts[account_number]['Loans'] = []

        accounts[account_number]['Loans'].append({
            'loan_amount': loan_amount,
            'loan_interest_rate': loan_interest_rate,
            'total_payable_amount': total_payable_amount,
            'decision': decision,
        })
        return True
    else:
        print("Invalid account number. Please enter a valid account number.")
    return False

def generate_loan_schedule(account_number, loan_amount, loan_interest_rate):
    monthly_interest_rate = loan_interest_rate / 12
    total_months = 12 
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_months))

    schedule = []
    remaining_balance = loan_amount
    for month in range(1, total_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        schedule.append({'Month': month, 'Payment Date': (datetime.now() + timedelta(days=month * 30)).strftime("%Y-%m-%d"), 'Principal': principal_payment, 'Interest': interest_payment, 'Balance': remaining_balance})

    with open(f'loan_schedule_{account_number}.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Month', 'Payment Date', 'Principal', 'Interest', 'Balance'])
        writer.writeheader()
        writer.writerows(schedule)

def balance(accounts):
    account_number = input("Enter your account number: ")

    if account_number in accounts:
        loan_amount = float(input("Enter Your loan amount: "))
        loan_interest_rate = 0.09
        total_payable_amount = loan_amount + (loan_amount * loan_interest_rate)
        print(f"Your loan interest rate is {loan_interest_rate * 100}%, Total payable amount is {total_payable_amount}.")
        decision = int(input("Do you want to take a loan? Press 1 for Yes, 2 for No: "))

        try:
            if add_funds(account_number, loan_amount, loan_interest_rate, total_payable_amount, decision, accounts):
                with open('database.py', 'w') as f:
                    f.write('database = ' + str(database))
                return True
        except ValueError:
            print("Invalid amount entered. Please enter a valid number.")
    else:
        print("Invalid account number. Please enter a valid account number.")
    return False

if __name__ == "__main__":
    balance(database)
