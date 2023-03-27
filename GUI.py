import tkinter as tk
from tkinter import messagebox
from bank import Bank, Account

class CreateAccountPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # create account label
        
        self.title("Create new account")
        self.geometry("350x300")
        self.bank = parent.bank
        
        # create form for creating a new account
        tk.Label(self, text="Create Account").pack(pady=10)
        tk.Label(self, text="Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=7)

        tk.Label(self, text="Set password").pack()
        self.balance_entry = tk.Entry(self)
        self.balance_entry.pack(pady=7)

        tk.Label(self, text="Initial Balance").pack()
        self.balance_entry = tk.Entry(self)
        self.balance_entry.pack(pady=7)

        tk.Button(self, text="Create", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.create_account).pack(pady=10)
        
        tk.Button(self, text="Back", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.destroy).pack(pady=10)

    def create_account(self):
        name = self.name_entry.get().strip()
        balance_str = self.balance_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Name cannot be empty")
            return
        try:
            balance = float(balance_str)
        except ValueError:
            messagebox.showerror("Error", "Balance must be a number")
            return
        account = self.bank.create_account(name, balance)
        
        tk.messagebox.showinfo("Account info", f"Account with details {account} created ")
        

class ViewAccountPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("View account")
        self.geometry("350x300")
        self.bank = parent.bank

        tk.Label(self, text="Account id:").grid(row=0, column=0, padx=5, pady=5)
        self.account_entry = tk.Entry(self)
        self.account_entry.grid(row=0, column=1)

        tk.Label(self, text="Account password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Close button
        tk.Button(self, text="Open", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.view_account).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self, text="Back", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.destroy).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def view_account(self):
        account_id = self.account_entry.get().strip()
       
        account = self.bank.get_account(int(account_id))
        print(account)
        if account is None:
            tk.messagebox.showerror("Error", f"Account with ID {account_id} does not exist")
        else:
            
            tk.messagebox.showinfo("Accunt details", f" {account} ")
        #     self.destroy()
        # self.transient(master)
        # self.grab_set()
        # master.wait_window(self)

class TransferPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Transfer funds")
        self.geometry("350x300")
        self.bank = parent.bank
        # Account information labels
        tk.Label(self, text="Sender id:").grid(row=0, column=0)
        self.sender_entry = tk.Entry(self)
        self.sender_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Sender password:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Transfer form labels and inputs
        tk.Label(self, text="Recipient id:").grid(row=3, column=0, padx=5, pady=5)
        self.recipient_entry = tk.Entry(self)
        self.recipient_entry.grid(row=3, column=1, padx=5, pady=5)
        tk.Label(self, text="Transfer amount:").grid(row=4, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Transfer button
        tk.Button(self, text="Transfer",  width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.transfer).grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self, text="Back", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.destroy).grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        
    def transfer(self):
        account1_id = self.sender_entry.get()
        account2_id = self.recipient_entry.get()

        account1 = self.bank.get_account(int(account1_id))
        account2 = self.bank.get_account(int(account2_id))
        amount = float(self.amount_entry.get())

        if account1 and account2:
            try:
                self.bank.transfer(account1_id, account2_id, amount)
                tk.messagebox.showinfo("Fund transfer",f"Fund transfer of {amount} successful.Funds transferred to {account2_id}.")
                
                self.destroy()
            except ValueError as e:
                print(str(e))
        else:
            tk.messagebox.showerror("Error", f"Enter valid account")


class DepositPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Deposit")
        self.geometry("350x300")
        self.bank = parent.bank
        
        # create form for depositing
        tk.Label(self, text="Deposit").pack(pady=10)
        tk.Label(self, text="Account ID").pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)
        tk.Label(self, text="Amount").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        tk.Button(self, text="Deposit", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.deposit).pack(pady=10)
        tk.Button(self, text="Back", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.destroy).pack(pady=10)

    def deposit(self):
        id = int(self.id_entry.get())
        amount = float(self.amount_entry.get())
        account = self.bank.get_account(id)
        if account is None:
            tk.messagebox.showerror("Error", f"Account with ID {id} does not exist")
        else:
            self.bank.deposit(id,amount)
            tk.messagebox.showinfo("Deposit Successful", f"Deposited {amount} into account {id}.")
            self.destroy()

class WithdrawPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Withdraw")
        self.geometry("350x300")

        # create form for withdrawing from an account
        tk.Label(self, text="Withdraw from Account").pack(pady=10)
        tk.Label(self, text="Account ID").pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)
        tk.Label(self, text="Amount").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # create withdraw button
        tk.Button(self, text="Withdraw", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.withdraw).pack(pady=10)
        tk.Button(self, text="Back", width=15, height=1, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.destroy).pack(pady=10)


    def withdraw(self):
        # get account ID and amount
        account_id = int(self.id_entry.get())
        amount = float(self.amount_entry.get())

        # call withdraw function from bank and display message
        try:
            self.parent.bank.withdraw(account_id, amount)
            tk.messagebox.showinfo("Withdraw", f"{amount} withdrawn from account {account_id}")
            self.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Withdraw", str(e))

class BankGUI(tk.Tk):
    def __init__(self, bank):
        super().__init__()
        self.bank = bank
        self.title("Banking System")
        self.geometry("800x600")
        
        # create main menu frame
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(pady=20)
        
        # create basic function buttons
        tk.Button(self.menu_frame, text="Create Account", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.create_account_page, relief=tk.FLAT).grid(row=0, column=0, padx=10, pady=30)
        tk.Button(self.menu_frame, text="Deposit", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white',  command=self.deposit_page, relief=tk.FLAT).grid(row=0, column=1, padx=10, pady=30)
        tk.Button(self.menu_frame, text="Withdraw", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.withdraw_page, relief=tk.FLAT).grid(row=1, column=0, padx=10, pady=30)
        tk.Button(self.menu_frame, text="Transfer", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.transfer_page, relief=tk.FLAT).grid(row=1, column=1, padx=10, pady=30)
        tk.Button(self.menu_frame, text="View Account", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.view_account_page, relief=tk.FLAT).grid(row=2, column=0, padx=10, pady=30)
        tk.Button(self.menu_frame, text="Exit", width=20, height=2, font=('Arial', 12), bg='#ff6666', fg='white', command=self.quit, relief=tk.FLAT).grid(row=2, column=1, padx=10, pady=30)
        
        # create container frame for pages
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # create initial page
        # self.create_account_page()
        
    def create_account_page(self):
    # clear container frame
        CreateAccountPage(self)

        
    def deposit_page(self):
    # clear container frame
        DepositPage(self)
        
    def withdraw_page(self):
        # implementation of withdraw page
        WithdrawPage(self)
    
    def transfer_page(self):
        TransferPage(self)
    
    def view_account_page(self):
        # implementation of view account page
        ViewAccountPage(self)
    
if __name__ == "__main__":
    bank = Bank()
    gui = BankGUI(bank)
    gui.mainloop()
