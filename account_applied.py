from decimal import Decimal
from account import Account  # Assuming account.py is in the same directory

def main():
    # Create an Account object
    try:
        account = Account("John Doe", Decimal('100.00'))
    except ValueError as error:
        print(error)
        return

    # Deposit money into the account
    try:
        account.deposit(Decimal('50.00'))
    except ValueError as error:
        print(error)
        return

    # Print the account balance
    print(f"Account holder: {account.name}")
    print(f"Current balance: {account.balance}")

if __name__ == "__main__":
    main()