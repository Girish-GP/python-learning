# You are building a class to manage a BankAccount. The BankAccount class should store the account holder's name, the account balance, and perform basic banking operations such as deposits and withdrawals. The balance should always be computed dynamically, and the account holder's name should not be changed after it is set.

# Implement the BankAccount class with the following requirements:
# The account holder's name is a private attribute that can only be set during initialization, and it cannot be changed once set.
# The balance should also be a private attribute and should only be modified using the deposit and withdraw methods.
# The deposit method should increase the balance by a specified amount.
# The withdraw method should decrease the balance by a specified amount, but it should raise an exception if there are insufficient funds.
# The balance should never be negative, and the class should raise an exception if an invalid deposit or withdrawal amount is provided (e.g., negative amounts).
# A computed property called balance should return the current balance.
# The account holder's name and balance should not be directly accessed from outside the class, but should be accessed and modified through the provided methods and properties.

# Constraints:
# Ensure that the balance is always updated correctly.
# Ensure that no negative balance is allowed (i.e., no withdrawals that result in negative balances).
# Make sure that the account holder's name cannot be modified after initialization.
# Write the implementation of the BankAccount class.


class BankAccount:

    def __init__(self,account_holder_name):
        self._account_holder_name = None
        self._balance = 0
        self.account_holder_name = account_holder_name

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self,name):
        if self._account_holder_name is None:
            self.check_validation(name)
            self._account_holder_name = name
        else:
            raise Exception("Account holder name cannot be modified")
    
    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
       if not isinstance(amount, (int, float)) or amount <= 0:
            raise Exception("Invalid amount. Deposit must be a positive number.")
       else:
        self._balance += amount
        print(f"{amount} deposited and now the balance is {self._balance}")

    def withdraw(self,amount):
        if not isinstance(amount,(int,float)) or amount <=0:
            raise Exception("Invalid amount. Withdrawal must be a positive number.")
        if (self._balance - amount) < 0:
            raise Exception("Cannot withdraw. Insufficient Balance!")
        else:
            self._balance -= amount
            print(f"{amount} withdrawn and the remaining balance is {self._balance}")

    def check_validation(self,name):
        if len(name) < 3:
            raise Exception("Account holder name should consist of minimum 3 characters")
        elif len(name) > 20:
            raise Exception("Account holder name should not have more than 20 characters")
        elif not name.isalpha():
            raise Exception("Account holder name should only consist alphabets")


try:
    account1 = BankAccount("girish")
    print(account1.account_holder_name)
    # account1.account_holder_name = "Test" #Error: Account holder name cannot be modified
    account1.deposit(2000)
    account1.withdraw(1000)
except Exception as e:
    print(f"Error: {e}")
    