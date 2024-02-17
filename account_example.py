from account import Account
from decimal import Decimal 

account1 = Account('Nolan Moss', Decimal('1000.00'))

print(account1.name)
print(account1.balance)