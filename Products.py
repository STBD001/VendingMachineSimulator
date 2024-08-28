products = []


def Add_product():
    item = input("Enter the product name: ")
    try:
        price = float(input("Enter the product price: "))
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        return

    products.append((item.lower(), price))
    print(f"Added product: {item} with price: {price:.2f} $")


def Display_products():
    if not products:
        print("No products available.")
    else:
        print("Product List:")
        for item, price in products:
            print(f"Product: {item.capitalize()}, price: {price:.2f} $")


def Change_price():
    print("\nChange product price")
    item_to_change = input("Enter the name of the product to change the price: ").lower()

    product_found = False
    for i, (item, price) in enumerate(products):
        if item == item_to_change:
            try:
                new_price = float(input("Enter the new price: "))
                products[i] = (item, new_price)
                print(f"Price for product '{item.capitalize()}' updated to {new_price:.2f} $.")
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
            product_found = True
            break

    if not product_found:
        print(f"Product '{item_to_change.capitalize()}' was not found in the database.")