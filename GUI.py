import tkinter as tk

class BankingSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Banking System")

        # Create main page
        self.main_frame = tk.Frame(self.master, width=500, height=500)
        self.main_frame.pack()

        self.create_buttons()

        # Create second page
        self.second_frame = tk.Frame(self.master, width=500, height=500)
        self.create_second_page()

    def create_buttons(self):
        create_acc_btn = tk.Button(self.main_frame, text="Create Account", command=self.create_account)
        create_acc_btn.pack(pady=10)

        withdraw_btn = tk.Button(self.main_frame, text="Withdraw Cash", command=self.withdraw_cash)
        withdraw_btn.pack(pady=10)

        deposit_btn = tk.Button(self.main_frame, text="Deposit Cash", command=self.deposit_cash)
        deposit_btn.pack(pady=10)

        transfer_btn = tk.Button(self.main_frame, text="Transfer", command=self.transfer)
        transfer_btn.pack(pady=10)

        view_btn = tk.Button(self.main_frame, text="View Account Detail", command=self.view_account_detail)
        view_btn.pack(pady=10)

    def create_second_page(self):
        # Create a label and an entry field for the account number
        acc_num_label = tk.Label(self.second_frame, text="Account Number:")
        acc_num_label.pack(pady=10)

        acc_num_entry = tk.Entry(self.second_frame)
        acc_num_entry.pack(pady=10)

        # Create a label and an entry field for the amount to be transferred
        amount_label = tk.Label(self.second_frame, text="Amount:")
        amount_label.pack(pady=10)

        amount_entry = tk.Entry(self.second_frame)
        amount_entry.pack(pady=10)

        # Create a button for the transfer function
        transfer_btn = tk.Button(self.second_frame, text="Transfer", command=self.transfer_funds)
        transfer_btn.pack(pady=10)

    def create_account(self):
        # TODO: Implement create account functionality
        pass

    def withdraw_cash(self):
        # TODO: Implement withdraw cash functionality
        pass

    def deposit_cash(self):
        # TODO: Implement deposit cash functionality
        pass

    def transfer(self):
        self.main_frame.pack_forget()
        self.second_frame.pack()

    def transfer_funds(self):
        # TODO: Implement transfer funds functionality
        pass

    def view_account_detail(self):
        # TODO: Implement view account detail functionality
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = BankingSystemGUI(root)
    root.mainloop()
