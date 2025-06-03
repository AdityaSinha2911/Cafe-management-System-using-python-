menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 20,
    'Coffee': 60,
    'Cold-Drink': 40,
}

# Greet
print("Welcome to PYTHON Restaurant")
print('Pizza: Rs 40 \nPasta: Rs 50 \nBurger: Rs 20\nCoffee: Rs 60\nCold-Drink: Rs 40')

order_total = 0

item_1 = input("Enter the name of the item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is out of stock, will be available soon!")

another_order = input("Do you want to add another item? (Yes/No) ").lower()

while another_order == 'yes':
    item = input("Enter the name of the next item = ")
    
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Order item {item} is out of stock, will be available soon!")
    
    another_order = input("Do you want to add another item? (Yes/No) ").lower()

print("The total payable amount is Rs.", order_total)

