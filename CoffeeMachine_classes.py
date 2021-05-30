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
    """returns true when order can be made and false when not enough"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough



def process_coins():
    """returns the total calculated from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(amount_received, drink_cost):
    """return true when payment accepeted, or false when not enough money"""
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f'Here is {change} change')
        global profit
        profit += drink_cost
        return True
    else:
        print(f'Sorry not enough money.')
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} *emoji*')

is_on = True

# TODO 1. Ask the user what they want.
while is_on:
    choice = input(f'What would you like? (expresso, latte, cappucinno):')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])




# TODO 2. Turn coffee machine off when they want to maintain.
if choice == 'off':
    machine_on = False
    print("Machine is now turned off")

# TODO 3. Print report of resources. water, milk, coffee, money
print(f'Report before purchasing {choice}')
print(f'Water:', resources['water'],'ml')
print(f'Milk:', resources['milk'],'ml')
print(f'Coffee:', resources['coffee'],'g')

# TODO 7. Make Coffee

# def make_coffee(choice):
#     print(f'Report after purchasing', choice)
#     print(f'Here is your', choice,'Enjoy!')
#     # new_water = resources['water'] -
#
#     print(f'Water:', resources['new_water'], 'ml')
#     print(f'Milk:', resources['milk'], 'ml')
#     print(f'Coffee:', resources['coffee'], 'g')
#
# make_coffee(choice)
# TODO 4. check resources.



# TODO 5. Process coins


# TODO 6. Check transaction successful.

