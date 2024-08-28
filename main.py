from Products import Display_products, Add_product, Change_price

def main():

    while True:
        print("1. Product List")
        print("2. Add a product")
        print("3. Change price")
        print("4. Exit")
        choice = input("Choose your option: ")

        if choice == '1':
            print("product display")
            Display_products()
        if choice == '2':
            print("Adding products: ")
            Add_product()
        if choice == '3':
            print("change in product prices")
            Change_price()
        if choice == '4':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
