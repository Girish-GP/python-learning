# Let’s go through an example in a real-world scenario: A banking system.
# Imagine you're implementing a BankAccount class where the balance is a protected attribute. We want to ensure that:
# The balance is always non-negative when set.
# The balance is calculated with interest when fetched.

class BankAccount:

    def __init__(self,balance,interest):
        self._balance = balance #protected attribute
        self._interest = interest

    @property
    def balance(self):
        # getter to retrive the balance
        return self._balance * (1 + self._interest)

    @balance.setter
    def balance(self,amount):
        # setter method to ensure that the balance is not negative
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    
account1 = BankAccount(1000,0.5)

print(account1.balance)

account1.balance = 1200

print(account1.balance)




