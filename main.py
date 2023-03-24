from bank import Bank, Account

def main():
    # create a bank object
    bank = Bank()

    while True:
        # display main menu
        print("==============================")
        print(" Welcome to MyBank Banking System ")
        print("==============================")
        print("Please select an option:")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. View account details")
        print("6. Exit")

        # get user input
        choice = input("Enter your choice (1-6): ")

        # process user choice
        if choice == "1":
            # create a new account
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = bank.create_account(name, balance)
            print(f"Account created with ID {account}")
        elif choice == "2":
            # deposit money
            account_id = int(input("Enter account ID: "))
            account = bank.get_account(account_id)
            if account:
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_id,amount)
                print(f"${amount:.2f} deposited into account {account_id}")
            else:
                print("Invalid account ID.")
            
        elif choice == "3":
            # withdraw money
            account_id = int(input("Enter account ID: "))
            account = bank.get_account(account_id)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_id,amount)
                print(f"${amount:.2f} withdrawn from account {account_id}")
            else:
                print("Invalid account ID.")
        # transfer money
        elif choice == "4":
            account1_id = int(input("Enter source account ID: "))
            account2_id = int(input("Enter destination account ID: "))
            
            account1 = bank.get_account(account1_id)
            account2 = bank.get_account(account2_id)
            
            if account1 and account2:
                amount = float(input("Enter transfer amount: "))
                bank.transfer(account1_id, account2_id, amount)
                
            else:
                print("Invalid account ID.")
                
        elif choice == "5":
            # view account details
            account_id = int(input("Enter account ID: "))
            account = bank.get_account(account_id)

            if account:
                print(account)
            else:
                print("Invalid account ID.")
        elif choice == "6":
            # exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
