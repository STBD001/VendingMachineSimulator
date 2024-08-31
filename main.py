import tkinter as tk
from Products import Display_products, Add_product, Change_price
from Money import Deposit_Money, Withdraw_Money, Buy_Item, Account_Balance

def main():
    root = tk.Tk()
    root.title("Vending Machine Simulator")
    root.geometry("320x205")

    btn_product_list = tk.Button(root, text="Product List", command=Display_products)
    btn_add_product = tk.Button(root, text="Add a product", command=Add_product)
    btn_change_price = tk.Button(root, text="Change price", command=Change_price)
    btn_account_balance = tk.Button(root, text="Account balance", command=Account_Balance)
    btn_deposit_money = tk.Button(root, text="Deposit money", command=Deposit_Money)
    btn_withdraw_money = tk.Button(root, text="Withdraw money", command=Withdraw_Money)
    btn_buy_item = tk.Button(root, text="Buy item", command=Buy_Item)
    btn_exit = tk.Button(root, text="Exit", command=root.quit)

    btn_product_list.pack(fill='x')
    btn_add_product.pack(fill='x')
    btn_change_price.pack(fill='x')
    btn_account_balance.pack(fill='x')
    btn_deposit_money.pack(fill='x')
    btn_withdraw_money.pack(fill='x')
    btn_buy_item.pack(fill='x')
    btn_exit.pack(fill='x')

    root.mainloop()

if __name__ == "__main__":
    main()
