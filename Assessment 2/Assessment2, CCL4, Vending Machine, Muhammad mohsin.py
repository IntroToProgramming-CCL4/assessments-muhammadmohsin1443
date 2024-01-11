#Creative Computing Level 4
#Student name: Muhammad Mohsin
#student id: 2023741

#Assessment 2, Utility app, The Vending machine
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Hi There!-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("\n###################/#################################\####################")
print("==================/===================================\===================")
print("-----------------/-Welcome~to~Al-Obese~Vending~Machine-\------------------")
print("\n________________/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\_________________")
print("***************/*****************************************\****************")


# Writing the function that will be displaying our menu
def display_menu():
    print("\n\n\n=========/\= Menu =/\=========")
    for category, items in menu.items():
        print(f"{category}:")
        for code, details in items.items():
            print(f"  {code}: {details['item']} - $AED{details['price']:.2f}")

# Writing a Function which will process the user's purchase information
def process_purchase(selected_item, money_inserted):
    if selected_item in item_codes:
        item_details = item_codes[selected_item]
        if money_inserted >= item_details['price']:
            change = money_inserted - item_details['price']
            print(f"Dispensing {item_details['item']}")
            print(f"Change: $AED{change:.2f}")
            

            # Suggesting an extra item to the user for a better experience
            money_inserted = suggest_extra_item(money_inserted)

            return True
        else:
            print("\nSorry, the inserted credit is insufficient. Please insert more money.")
    else:
        print("\nDear customer, the item code inserted is invalid. Please enter a valid code.")

    return False

import random
# Making a function that would sudgest the user to buys some thing as an add-on at a full price
def suggest_extra_item(money_inserted):
    print("\nWe would like to give you a free gift from our menu, would you like to proceed? ")
    extra_item = input("Enter 'yes' or 'no': ").lower()
    if extra_item == 'yes':
        print("\nGreat ! ")
        # Defining sudgested items
        suggested_items = {
            'Drinks': 'Pepsi (330ml)',
            'Snacks': 'Ding Dong Mixed Nuts (100g)',
            'Chocolate': 'Kit Kat',
            'Chips': 'Lays Maxx Mexican Chill',
            'Candies': 'Chupa Chups Lolipop'
        }

        # Writing a function that will randomly select a category for suggestion
        suggested_category = random.choice(list(suggested_items.keys()))

        # Now we will Display the specific item from the suggested category
        suggested_item = suggested_items[suggested_category]

        print(f"\n\nWe have {suggested_item} from the {suggested_category} category as a Free gift for you!")

        # Then asking the user if they want to add the suggested item
        add_suggested_item = input("\nDo you want to add this Free gift to your purchase? Enter 'yes' or 'no': ").lower()

        if add_suggested_item == 'yes':
            # Find the item code in the menu
            for code, details in item_codes.items():
                if details['item'] == suggested_item:
                    suggested_item_code = code
                    break
            else:
                suggested_item_code = None

            if suggested_item_code:
                print(f"\nAdding {suggested_item} to your purchase.")
            
            else:
                print("\nError: Item code not found for the suggested item.")

    return money_inserted

# Creating a full detailed menu, 5 categories of edible and drinkable stuff, each category having 10 items, with their quantity(grams or milliliter) 
menu = {
    'Drinks': {
        '001': {'item': 'Coca Cola (330ml)', 'price': 2.50},
        '002': {'item': 'Pepsi (330ml)', 'price': 2.50},
        '003': {'item': 'Thumbs up (330ml)', 'price': 2.50},
        '004': {'item': 'Mai Dubai Water (500ml)', 'price': 1.00},
        '005': {'item': 'Lipton Iced Tea (330ml)', 'price': 3.75},
        '006': {'item': 'Nescafe Original Cold Coffee (240ml)', 'price': 8.00},
        '007': {'item': 'Fresh Barakat Orange Juice (300ml)', 'price': 7.75},
        '008': {'item': 'Fresh Barakat Apple Juice (500ml)', 'price': 10.50},
        '009': {'item': 'Al-Maraai Premium Mango Milk (225ml)', 'price': 2.65},
        '010': {'item': 'Al-Rawabi Lemon and mint (200ml)', 'price': 2.65},
    },
    'Snacks': {
        '011': {'item': 'Sunflower Seeds (75g)', 'price': 1.30},
        '012': {'item': 'Ding Dong Mixed Nuts (100g)', 'price': 3.20},
        '013': {'item': ' Papa Joe Caramel Popcorn (140g)', 'price': 4.80},
        '014': {'item': 'Salted Penuts (300g)', 'price': 11.80},
        '015': {'item': 'Puck Cheese Sticks (108g)', 'price': 11.50},
        '016': {'item': 'Musc;e Core High Protien Bar Chocolate 27g Protien (65g)', 'price': 15.75},
        '017': {'item': 'Cocomo Filled Biscuits (35g)', 'price': 1.70},
        '018': {'item': 'Dry Fruits (Almonds, Cashew, Dates, Apricot, Walnuts, Fig, Rasins) (250g)', 'price': 14.60},
        '019': {'item': 'Jack Links Beef Jerky Original (40g)', 'price': 15.70},
        '020': {'item': 'Rice Cakes plain unsalted (100g)', 'price': 12.75},
    },
    'Chocolate': {
        '021': {'item': 'Dairy Milk', 'price': 1.80},
        '022': {'item': 'Kit Kat', 'price': 2.00},
        '023': {'item': 'Galaxy', 'price': 1.90},
        '024': {'item': 'Mars', 'price': 1.50},
        '025': {'item': 'Dairy Milk hazelnut', 'price': 2.20},
        '026': {'item': 'Bounty', 'price': 1.70},
        '027': {'item': 'Twix', 'price': 2.50},
        '028': {'item': 'Toblerone', 'price': 1.60},
        '029': {'item': 'Hersheys dark chocolate', 'price': 2.10},
        '030': {'item': 'Ferrero', 'price': 2.30},
    },
    'Chips': {
        '031': {'item': 'Oman Chips', 'price': 1.00},
        '032': {'item': 'Sohar Chips', 'price': 1.80},
        '033': {'item': 'Raja Vegetable cips', 'price': 1.20},
        '034': {'item': 'Kurkuray Masala', 'price': 2.50},
        '035': {'item': 'Slanty ', 'price': 4.00},
        '036': {'item': 'Lays Maxx Mexican Chill', 'price': 7.50},
        '037': {'item': 'Pringles BBQ', 'price': 8.30},
        '038': {'item': 'Tiffany Finns', 'price': 5.70},
        '039': {'item': 'Tiffany Bugles', 'price': 3.80},
        '040': {'item': 'Al Jufair Salad Chips', 'price': 2.50},
    },

    'Candies': {
        '041': {'item': 'Haribo Gummy Bears', 'price': 1.20},
        '042': {'item': 'Tiffany Mintz', 'price': 1.30},
        '043': {'item': 'Mackintoshs Quality Street Chocolate', 'price': 3.50},
        '044': {'item': 'Chupa Chups Lolipop', 'price': 1.10},
        '045': {'item': 'Werthers Original Cream Candies', 'price': 1.80},
        '046': {'item': 'Mintos', 'price': 1.00},
        '047': {'item': 'Skittles', 'price': 2.00},
        '048': {'item': 'Fruittella', 'price': 2.20},
        '049': {'item': 'Juicy Drop Blasts', 'price': 1.60},
        '050': {'item': 'Maltersers', 'price': 1.40},
    },
}

# so now we are going to create a dictionary to map item codes to their details
item_codes = {}
for category, items in menu.items():
    for code, details in items.items():
        item_codes[code] = details

# Displaying the menu
display_menu()

# writing a function that will take usser input for money
money_inserted = float(input("\nEnter money: $AED"))

# then we'll take the user input for the selection of items from our menu
selected_item = input("\nEnter the code of an item that you would want to purchase: ")

# writing a function that processes the purchase
transaction_completed = process_purchase(selected_item, money_inserted)

# writing to desplay the ending message when the user finished the transaction either successful or failed
if transaction_completed:
    print("\nThank you for using Al-Obese Vending Machine! Please collect your items below and change from the receipt box.")
    print("\n\nFollow us on our social media platforms: Instagram , Facebook , Twitter , Youtube , LinkedIn .")
    
else:
    print("\nDear Customer the Transaction is failed. Please try again.")


# now we are going to write a function that updates the stock of vending machine after a successful purchase
def update_stock(selected_item):
    category, code = get_category_and_code(selected_item)
    menu[category][code]['stock'] -= 1

# Writing a function so that we get the category and code from the selected item
def get_category_and_code(selected_item):
    for category, items in menu.items():
        for code in items.keys():
            if code == selected_item:
                return category, code

# Now we'll write a function that checks and displays the stock of items avilabe to the user
def display_stock():
    print("\n\n=========\/= Stock Status =\/=========")
    for category, items in menu.items():
        print(f"{category}:")
        for code, details in items.items():
            print(f"  {details['item']} - Stock: {details.get('stock', 'Unlimited')}")

# now a function that adds stock information to the menu, in front of every item in the menu, it will display how many are left, total stock per item is 10pc
for category, items in menu.items():
    for code, details in items.items():
        details['stock'] = 10  
# 10 is Setted as an initial stock for each item

# Main program loop, this will show up after a successful transaction and after fail transaction too after displaying :"Dear Customer the Transaction is failed. Please try again."
while True:
    # A classic Function to display the menu
    display_menu()

    # Again writing a function that will take usser input for money
    money_inserted = float(input("\nEnter money: $AED"))

    # Again we'll take the user input for the selection of items from our menu
    selected_item = input("\nEnter the code of an item that you would want to purchase: ")

    # again writing a function that processes the purchase
    transaction_completed = process_purchase(selected_item, money_inserted)

    # now a function writing to update stock if the transaction is successful
    if transaction_completed:
        update_stock(selected_item)

    # Now We'll write a function that will display the ending message
    if transaction_completed:
        print("\n\nThank you for using Al Obese Vending Machine! Please collect your items and change.")
        display_stock()  # This function will display the stock status after each successful transaction
    else:
        print("\n\nDear Customer the Transaction is failed. Please try again.")

    # Now at the end we'll ask the user if they want to make another purchase
    another_purchase = input("\nWould you like to make another purchase? (yes/no): ").lower()
    if another_purchase != 'yes':
        break
