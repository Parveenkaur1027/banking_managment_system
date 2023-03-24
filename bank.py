'''
In this updated implementation, we have used Encapsulation to hide the account balance and name attributes 
of the Account class by making them private (__balance and __name). We also used the get_id(), get_name(),
 and get_balance() methods to provide public access to these private attributes.

We have also demonstrated Polymorphism by creating a new SavingsAccount class that inherits from the Account class
 and has a different interest rate attribute.

Finally, we have used Inheritance by making SavingsAccount a subclass of Account. This allows us to reuse the 
code from the Account class and add new functionality specific to the SavingsAccount class.
'''

class Account:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account ID: {self.__id}\nName: {self.__name}\nBalance: {self.__balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, id, name, balance):
        super().__init__(id, name, balance)
        self.__interest_rate = 0.01

    def get_interest_rate(self):
        return self.__interest_rate

class Bank:
    def __init__(self):
        self.__accounts = []
        self.__next_id = 1

    def create_account(self, name, initial_deposit):
        account = Account(self.__next_id, name, initial_deposit)
        self.__accounts.append(account)
        self.__next_id += 1
        return account

    def create_savings_account(self, name, initial_deposit):
        account = SavingsAccount(self.__next_id, name, initial_deposit)
        self.__accounts.append(account)
        self.__next_id += 1
        return account

    def get_account(self, id):
        for account in self.__accounts:
            if account.get_id() == id:
                return account
        return None

    def deposit(self, id, amount):
        account = self.get_account(id)
        if account:
            balance = account.get_balance()
            balance += amount
            account._Account__balance = balance
        else:
            print("Account not found")

    def withdraw(self, id, amount):
        account = self.get_account(id)
        if account:
            balance = account.get_balance()
            if balance >= amount:
                balance -= amount
                account._Account__balance = balance
            else:
                print("Insufficient balance")
        else:
            print("Account not found")

    def transfer(self, sender_id, recipient_id, amount):
        sender = self.get_account(sender_id)
        recipient = self.get_account(recipient_id)
        if sender and recipient:
            sender_balance = sender.get_balance()
            if sender_balance >= amount:
                sender_balance -= amount
                sender._Account__balance = sender_balance
                recipient_balance = recipient.get_balance()
                recipient_balance += amount
                recipient._Account__balance = recipient_balance
                print("Transfer succeccful")
            else:
                print("Insufficient balance")
        else:
            print("Account not found")
