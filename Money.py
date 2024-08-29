money = 10
from  Products import products

def Account_Balance():
    print(f"Your account balance is {money: .2f}$")

def Deposit_Money():
    global money
    depo_money=float(input("Please enter how much money you want to deposit into your account: "))
    money+=depo_money
    money = round(money, 2)
    print(f"Your current account balance is: {money}$")
def Withdraw_Money():
    global money
    with_money=float(input("Write how much money you want to withdraw: "))
    if with_money>money:
        print("Sorry, you want to withdraw more funds but you do not have them in your account.")
    else:
        money-=with_money
        money = round(money, 2)
        print(f"Your current account balance is: {money}$")

def Buy_Item():
    global money
    wtb = input("Enter the name of the product you want to buy: ").lower()

    product_found = False
    for i, (item, price) in enumerate(products):
        print(f"Checking item: {item}, price: {price}")
        if item == wtb:
            if money >= price:
                money -= price
                print(f"Your {item.capitalize()} is ready!")
                products.pop(i)
            else:
                print("You do not have enough money to buy this item.")
            product_found = True
            break

    if not product_found:
        print(f"Product '{wtb.capitalize()}' was not found in the database.")
