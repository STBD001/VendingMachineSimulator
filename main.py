from Products import Display_products, Add_product, Change_price
from Money import Account_Balance, Deposit_Money, Withdraw_Money, Buy_Item
def main():

    while True:
        print("1. Product List")
        print("2. Add a product")
        print("3. Change price")
        print("4. Account balance")
        print("5. Deposit money")
        print("6. Withdraw money")
        print("7. Buy item")
        print("8. Exit")
        choice = input("Choose your option: ")

        if choice == '1':
            print("Product display")
            Display_products()
        if choice == '2':
            print("Adding products: ")
            Add_product()
        if choice == '3':
            print("Change in product prices")
            Change_price()
        if choice == '4':
            Account_Balance()
        if choice =='5':
            Deposit_Money()
        if choice =='6':
            Withdraw_Money()
        if choice == '7':
            Buy_Item()
        if choice == '8':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
