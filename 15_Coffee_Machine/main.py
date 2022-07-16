from art import logo2

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarter?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(amount_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient"""
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        print("$", amount_received)
        print("$", drink_cost)
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


def login():
    user_id = input("Enter Your User ID : ")
    password = input("Enter Your Password : ")
    if user_id == 'Admin' and password == 'nimda':
        return True
    else:
        return False


print(logo2)
is_on = login()  # True
while is_on:
    user_choice = input("What would you like?(espresso,latte,cappuccino): ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {profit}")
    elif user_choice == 'refill':
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
