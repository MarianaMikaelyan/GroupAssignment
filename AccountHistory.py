
history = {}

def save_transaction(account_number, transaction_detail):
    if account_number in history:
        history[account_number].append(transaction_detail)
    else:
        history[account_number] = [transaction_detail]


if __name__ == "__main__":
    save_transaction()
