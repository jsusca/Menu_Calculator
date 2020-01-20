"""
GOAL
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since
your restaurant only sells 9 different items, you assign each one to a number, as shown below.

Chicken Strips - $3.50

French Fries - $2.50

Hamburger - $4.00

Hotdog - $3.50

Large Drink - $1.75

Medium Drink - $1.50

Milk Shake - $2.25

Salad - $3.75

Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers and then it should
calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog,
and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also,
make sure that the program loops so the user can take multiple orders without having to restart the program each time.

SUB-GOALS
- If you decide to, print out the items and prices every time before the user types in an order.
- Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. If
an item was not ordered at all, then it should not show up.
"""


# Define function to split user input into list of characters
def split(user_input):
    return [char for char in user_input]


# Create menu with item number, item name and item price
menu = {
    1: {"item": "Chicken Strips", "price": 3.50},
    2: {"item": "French Fries", "price": 2.50},
    3: {"item": "Hamburger", "price": 4.00},
    4: {"item": "Hotdog", "price": 3.50},
    5: {"item": "Salad", "price": 3.75},
    6: {"item": "Small Drink", "price": 1.25},
    7: {"item": "Medium Drink", "price": 1.50},
    8: {"item": "Large Drink", "price": 1.75},
    9: {"item": "Milk Shake", "price": 2.25}
}

running = True

print("\nWelcome to the Menu Calculator!\n")

# Create program within while loop to continue running after use
while running:
    prices = []
    order = []
    i = 0

    # Print menu (item number, item, price)
    for item_num, item_dict in menu.items():
        item_name = item_dict['item']
        item_price = item_dict['price']
        print(f'{item_num}. {item_name} ${item_price:.2f}')

    choice = input("\nPlease enter order as a series of item numbers without any spaces.\nFor example, to order "
                   "a hamburger with fries and a small drink, \nyou would type: 239, and the program would output "
                   "the total cost of $8.75.\n")

    # Split user input into list of item numbers
    choice = split(str(choice))

    # Iterate through list of user-input item numbers, and add
    # corresponding dictionaries (item name: item price) to a list
    for num in choice:
        order.append(menu[int(num)])
    counter = 0

    # Iterate through list of item dictionaries
    for dictionary in order:
        for order_name, order_price in dictionary.items():  # Iterate through item dictionaries
            counter += 1  # Increment counter
            if counter == 2:  # If iterating through item price (index 2):
                prices.append(order_price)  # Add price to a list
                counter = 0  # Reset counter

    print(prices)
    # Sum price list and print
    print(f"Total cost: ${sum(prices):.2f}\n")
