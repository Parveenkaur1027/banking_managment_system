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


def create_account():
    account_number = input("Enter account number: ")
    account_holder_name = input("Enter account holder name: ")
    account_balance = float(input("Enter account balance: "))
    account_type = input("Enter account type (1 for savings, 2 for current): ")
    if account_type == "1":
        interest_rate = float(input("Enter interest rate: "))
        minimum_balance = float(input("Enter minimum balance: "))
        account = SavingsAccount(account_number, account_holder_name, account_balance, interest_rate, minimum_balance)
    else:
        account = BankAccount(account_number, account_holder_name, account_balance)

    accounts.append(account)
    print("Account created successfully")


def display_account_details(account):
    print("Account Number: ", account.get_account_number())
    print("Account Holder Name: ", account.get_account_holder_name())
    print("Account Balance: ", account.get_account_balance())


# Main Menu
accounts = []

while True:
    print("\n\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Account Details")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        account_number = input("Enter account number: ")
        account = next((acc for acc in accounts if acc.get_account_number() == account_number), None)
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print("Deposit successful")
        else:
            print("Deposit failed")
