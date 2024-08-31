import tkinter as tk

money = 10.0  # Przykładowy balans konta
from Products import products

def Account_Balance():
    Account_window = tk.Toplevel()
    Account_window.title("Account Balance")

    lbl = tk.Label(Account_window, text="Account Balance:", font=("Arial", 14))
    lbl.pack(pady=10)

    balance_label = tk.Label(Account_window, text=f"Your account balance is {money:.2f} $", font=("Arial", 12))
    balance_label.pack(padx=10, pady=10)

def Deposit_Money():
    def deposit():
        try:
            depo_money = float(depo_entry.get().strip())
            global money
            money += depo_money
            money = round(money, 2)
            result_label.config(text=f"Your current account balance is: {money:.2f}$", fg="green")
        except ValueError:
            result_label.config(text="Please enter a valid number.", fg="red")

    deposit_window = tk.Toplevel()
    deposit_window.title("Deposit Money")

    lbl = tk.Label(deposit_window, text="Enter amount to deposit:", font=("Arial", 14))
    lbl.pack(pady=10)

    depo_entry = tk.Entry(deposit_window, width=30)
    depo_entry.pack(padx=10, pady=5)

    deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit)
    deposit_button.pack(pady=10)

    result_label = tk.Label(deposit_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)

def Withdraw_Money():
    def withdraw():
        try:
            with_money = float(with_entry.get().strip())
            global money
            if with_money > money:
                result_label.config(text="Insufficient funds in your account.", fg="red")
            else:
                money -= with_money
                money = round(money, 2)
                result_label.config(text=f"Your current account balance is: {money:.2f}$", fg="green")
        except ValueError:
            result_label.config(text="Please enter a valid number.", fg="red")

    withdraw_window = tk.Toplevel()
    withdraw_window.title("Withdraw Money")

    lbl = tk.Label(withdraw_window, text="Enter amount to withdraw:", font=("Arial", 14))
    lbl.pack(pady=10)

    with_entry = tk.Entry(withdraw_window, width=30)
    with_entry.pack(padx=10, pady=5)

    withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw)
    withdraw_button.pack(pady=10)

    result_label = tk.Label(withdraw_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)

def Buy_Item():
    def buy():
        wtb = item_entry.get().strip().lower()
        global money

        product_found = False
        for i, (item, price) in enumerate(products):
            if item == wtb:
                if money >= price:
                    money -= price
                    money = round(money, 2)
                    products.pop(i)
                    result_label.config(text=f"Your {item.capitalize()} is ready! Current balance: {money:.2f}$", fg="green")
                else:
                    result_label.config(text="You do not have enough money to buy this item.", fg="red")
                product_found = True
                break

        if not product_found:
            result_label.config(text=f"Product '{wtb.capitalize()}' was not found in the database.", fg="red")

    buy_window = tk.Toplevel()
    buy_window.title("Buy Item")

    lbl = tk.Label(buy_window, text="Enter the product name you want to buy:", font=("Arial", 14))
    lbl.pack(pady=10)

    item_entry = tk.Entry(buy_window, width=30)
    item_entry.pack(padx=10, pady=5)

    buy_button = tk.Button(buy_window, text="Buy", command=buy)
    buy_button.pack(pady=10)

    result_label = tk.Label(buy_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)
