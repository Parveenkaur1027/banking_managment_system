class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def set_account_holder_name(self, account_holder_name):
        self.__account_holder_name = account_holder_name

    def get_account_balance(self):
        return self.__account_balance

    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            print("Insufficient balance")
        else:
            self.__account_balance -= amount

    def transfer(self, amount, destination_account):
        if amount > self.__account_balance:
            print("Insufficient balance")
        else:
            self.__account_balance -= amount
            destination_account.deposit(amount)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, account_balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder_name, account_balance)
        self.__interest_rate = interest_rate
        self.__minimum_balance = minimum_balance

    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def get_minimum_balance(self):
        return self.__minimum_balance

    def set_minimum_balance(self, minimum_balance):
        self.__minimum_balance = minimum_balance

    def add_interest(self):
        interest = self.__account_balance * self.__interest_rate / 100
        self.__account_balance += interest


# Example usage
account1 = BankAccount("123456", "John Smith", 1000)
account2 = BankAccount("654321", "Jane Doe", 500)

# deposit
account1.deposit(500)
print(account1.get_account_balance())

# withdraw
account1.withdraw(200)
print(account1.get_account_balance())

# transfer
account1.transfer(300, account2)
print(account1.get_account_balance())
print(account2.get_account_balance())

# savings account
savings_account = SavingsAccount("789123", "Alice Jones", 5000, 1.5, 1000)
savings_account
