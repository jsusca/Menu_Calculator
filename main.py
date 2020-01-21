import re


# Define function to split user input into list of characters
def split(user_input):
    return list(user_input)


# Create menu with item number, item name and item price
menu = {
    '1': {"name": "Chicken Strips", "price": 3.50, "quantity_ordered": 0, "total_price": 0},
    '2': {"name": "French Fries", "price": 2.50, "quantity_ordered": 0, "total_price": 0},
    '3': {"name": "Hamburger", "price": 4.00, "quantity_ordered": 0, "total_price": 0},
    '4': {"name": "Hotdog", "price": 3.50, "quantity_ordered": 0, "total_price": 0},
    '5': {"name": "Salad", "price": 3.75, "quantity_ordered": 0, "total_price": 0},
    '6': {"name": "Small Drink", "price": 1.25, "quantity_ordered": 0, "total_price": 0},
    '7': {"name": "Medium Drink", "price": 1.50, "quantity_ordered": 0, "total_price": 0},
    '8': {"name": "Large Drink", "price": 1.75, "quantity_ordered": 0, "total_price": 0},
    '9': {"name": "Milk Shake", "price": 2.25, "quantity_ordered": 0, "total_price": 0}
}

running = True

print("\nWelcome to the Menu Calculator!\n")

# Create program within while loop to continue running after use
while running:
    prices = []
    order = {}
    i = 0
    overall_total = 0

    # Print menu (item number, item, price)
    for item_num, item_dict in menu.items():
        item_name = item_dict['name']
        item_price = item_dict['price']
        print(f'{item_num}. {item_name:<15} ${item_price:.2f}')

    choice = input("\nPlease enter order as a series of item numbers without any spaces.\nFor example, to order "
                   "a hamburger with fries and a small drink, \nyou would type: 239, and the program would output "
                   "the total cost of $8.75.\n")

    # Scrub user input so choice is only ints
    choice = re.sub(r'[^\d]', '', choice)
    choice = re.sub(r'0', '', choice)

    # Restart program if user doesn't input only ints
    if choice == '':
        continue

    # Split user input into list of item numbers
    choice = split(choice)

    for num in choice:  # Iterate through list of user-input item numbers
        if num not in order:  # If number is not in order
            order[num] = menu[num].copy()  # Add copy of item dictionary to order dictionary
        order[num]['quantity_ordered'] += 1  # If item choice is in order, increment item quantity
        order[num]['total_price'] += order[num]['price']  # And add item price to total_price value

    print(f'\n Item name     Price        Quantity      Total Price')

    # Print [item name, item price, number of items ordered, total price of quantity ordered]
    for item in order.values():
        overall_total += item['total_price']  # Add item total_prices to overall__total
        n = item['name']
        q = item['quantity_ordered']
        p = item['price']
        t = item['total_price']
        print(f'{n: <15}${p:<15.2f}{q: <15}${t:<15.2f}')

    print(f'     --- The order total is ${overall_total:0.2f} ---\n')
