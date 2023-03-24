import tkinter as tk
from bank import Bank, Account

class BankGUI(tk.Tk):
    def __init__(self, bank):
        super().__init__()
        self.bank = bank
        self.title("Banking System")
        self.geometry("500x300")
        
        # create main menu frame
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(pady=20)
        
        # create basic function buttons
        tk.Button(self.menu_frame, text="Create Account", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.create_account_page, relief=tk.FLAT).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Deposit", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.deposit_page, relief=tk.FLAT).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Withdraw", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.withdraw_page, relief=tk.FLAT).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Transfer", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.transfer_page, relief=tk.FLAT).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.menu_frame, text="View Account", width=20, height=2, font=('Arial', 12), bg='#66c2ff', fg='white', command=self.view_account_page, relief=tk.FLAT).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Exit", width=20, height=2, font=('Arial', 12), bg='#ff6666', fg='white', command=self.quit, relief=tk.FLAT).grid(row=1, column=2, padx=10, pady=10)
        
        # create container frame for pages
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # create initial page
        # self.create_account_page()
        
    def create_account_page(self):
    # clear container frame
        self.create_account_window = tk.Toplevel(self)
        self.create_account_window.title("Create Account")
        
        # create form for creating a new account
        tk.Label(self.create_account_window, text="Create Account").pack(pady=10)
        tk.Label(self.create_account_window, text="Name").pack()
        self.name_entry = tk.Entry(self.create_account_window)
        self.name_entry.pack(pady=5)
        tk.Label(self.create_account_window, text="Initial Balance").pack()
        self.balance_entry = tk.Entry(self.create_account_window)
        self.balance_entry.pack(pady=5)
        tk.Button(self.create_account_window, text="Create", command=self.create_account).pack(pady=10)
        tk.Button(self.create_account_window, text="Back", command=self.create_account_window.destroy).pack(pady=10)
        

    def create_account(self):
        name = self.name_entry.get().strip()
        balance_str = self.balance_entry.get().strip()
        if not name:
            tk.messagebox.showerror("Error", "Name cannot be empty")
            return
        try:
            balance = float(balance_str)
        except ValueError:
            tk.messagebox.showerror("Error", "Balance must be a number")
            return
        account = self.bank.create_account(name, balance)
        self.account_label.config(text=f"Account {account.id} created for {account.name} with balance {account.balance:.2f}")
        self.name_entry.delete(0, tk.END)
        self.balance_entry.delete(0, tk.END)

        
    def deposit_page(self):
        # implementation of deposit page
        pass
    
    def withdraw_page(self):
        # implementation of withdraw page
        pass
    
    def transfer_page(self):
        # implementation of transfer page
        pass
    
    def view_account_page(self):
        # implementation of view account page
        pass
    
if __name__ == "__main__":
    bank = Bank()
    gui = BankGUI(bank)
    gui.mainloop()
