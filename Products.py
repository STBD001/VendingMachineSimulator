import tkinter as tk

products = [("apple", 0.5), ("banana", 1.0), ("orange", 1.5)]

def add_product_to_list(item_entry, price_entry):
    item_name = item_entry.get().strip().lower()
    try:
        item_price = float(price_entry.get().strip())
    except ValueError:
        print("Price must be a number.")
        return

    if item_name and item_price > 0:
        products.append((item_name, item_price))
        print(f"Added product: {item_name}, price: {item_price:.2f} $")
    else:
        print("Product name cannot be empty, and price must be greater than 0.")

def Add_product():
    Add_window = tk.Toplevel()
    Add_window.title("Add Product")

    lbl = tk.Label(Add_window, text="Add product:", font=("Arial", 14))
    lbl.pack(pady=10)

    item_label = tk.Label(Add_window, text="Product name:")
    item_label.pack()
    item_entry = tk.Entry(Add_window, width=30)
    item_entry.pack(padx=10, pady=5)

    price_label = tk.Label(Add_window, text="Product price:")
    price_label.pack()
    price_entry = tk.Entry(Add_window, width=30)
    price_entry.pack(padx=10, pady=5)

    add_button = tk.Button(Add_window, text="Add to database",
                           command=lambda: add_product_to_list(item_entry, price_entry))
    add_button.pack(pady=10)

def Display_products():
    display_window = tk.Toplevel()
    display_window.title("Products List")

    lbl = tk.Label(display_window, text="Products List:", font=('Arial', 14))
    lbl.pack(pady=10)

    text_box = tk.Text(display_window, width=40, height=10, wrap='word')
    text_box.pack(padx=10, pady=10)

    if not products:
        text_box.insert('1.0', "No products available.")
    else:
        for item, price in products:
            text_box.insert('end', f"Product: {item.capitalize()}, price: {price:.2f} $\n")

    text_box.config(state='disabled')

def Change_price():
    change_window = tk.Toplevel()
    change_window.title("Change product price")

    lbl = tk.Label(change_window, text="Change product price:", font=("Arial", 14))
    lbl.pack(pady=10)

    item_label = tk.Label(change_window, text="Product name:")
    item_label.pack()
    item_entry = tk.Entry(change_window, width=30)
    item_entry.pack(padx=10, pady=5)

    price_label = tk.Label(change_window, text="New price:")
    price_label.pack()
    price_entry = tk.Entry(change_window, width=30)
    price_entry.pack(padx=10, pady=5)

    def update_price():
        item_to_change = item_entry.get().strip().lower()
        try:
            new_price = float(price_entry.get().strip())
        except ValueError:
            result_label.config(text="Price must be a number.", fg="red")
            return

        product_found = False
        for i, (item, price) in enumerate(products):
            if item == item_to_change:
                products[i] = (item, new_price)
                result_label.config(text=f"Price for product '{item.capitalize()}' has been updated.", fg="green")
                product_found = True
                break

        if not product_found:
            result_label.config(text=f"Product '{item_to_change.capitalize()}' was not found.", fg="red")

    change_button = tk.Button(change_window, text="Change price", command=update_price)
    change_button.pack(pady=10)

    result_label = tk.Label(change_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)
