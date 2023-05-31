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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.1,
    "quarters": 0.25,
}

turn_off_machine = False

while not turn_off_machine:
    print(f"Remaining resources: {resources}")

    user_choice = input("Which coffee would you like to drink, 'espresso', 'latte', or 'cappuccino'? If you don't want coffee, type 'off' to turn off the machine: ").lower()

    if user_choice == "off":
        turn_off_machine = True
        continue

    print("Please insert coins to pay.")

    if user_choice not in MENU:
        print("Invalid choice!")
        continue

    coins1 = input("How many pennies? ")
    coins2 = input("How many nickels? ")
    coins3 = input("How many dimes? ")
    coins4 = input("How many quarters? ")

    def paying_coffee(choice):
        total_pay = (float(coins1) * coins["pennies"]) + (float(coins2) * coins["nickels"]) + (float(coins3) * coins["dimes"]) + (float(coins4) * coins["quarters"])
        change = 0
        if total_pay >= MENU[choice]["cost"]:
            change1 = round(total_pay - MENU[choice]["cost"], 2)
            change += change1
            print(f"Thank you for payment. Here is your change: {change}")
            return True
        else:
            print(f"Sorry, this is not enough for your coffee. You can take your coins back: {total_pay}")
            return False

    if not paying_coffee(user_choice):
        continue


    def calculator(choice):
        if choice in MENU:
            ingredients = MENU[choice]["ingredients"]
            current_water = resources["water"]
            current_milk = resources["milk"]
            current_coffee = resources["coffee"]

            if current_water < ingredients.get("water", 0) or current_milk < ingredients.get("milk",
                                                                                             0) or current_coffee < ingredients.get(
                    "coffee", 0):
                print(f"Insufficient resources to make {choice}.")
                refill = input("Do you want to refill the resources? Type 'yes' or 'no': ").lower()
                if refill == "yes":
                    resources["water"] = 300
                    resources["milk"] = 200
                    resources["coffee"] = 100
                    print("Resources have been refilled.")
                return

            current_water -= ingredients.get("water", 0)
            current_milk -= ingredients.get("milk", 0)
            current_coffee -= ingredients.get("coffee", 0)

            resources["water"] = current_water
            resources["milk"] = current_milk
            resources["coffee"] = current_coffee

    calculator(user_choice)