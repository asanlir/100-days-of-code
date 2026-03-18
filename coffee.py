from coffee_menu import MENU, resources, coins


profit = 0
machine_on = True


def show_resources():
    """Shows the current resources of the coffee machine."""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(order_ingredients):
    """Checks if there are enough resources to make the coffee."""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def pay():
    """Handles the payment process."""

    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * coins["quarters"]
    total += int(input("How many dimes?: ")) * coins["dimes"]
    total += int(input("How many nickels?: ")) * coins["nickels"]
    total += int(input("How many pennies?: ")) * coins["pennies"]

    return total


def refill():
    """Manages the refilling of resources."""

    global resources
    fill = input("What would you like to refill? (water/milk/coffee): ").lower()
    if fill in resources:
        amount = int(input(f"How much {fill} would you like to add?: "))
        resources[fill] += amount
        print(f"{fill.capitalize()} refilled. Current {fill}: {resources[fill]}")
    else:
        print("Invalid resource. Please choose water, milk, or coffee.")


def make_coffee():
    """Processes the user's coffee order."""

    global profit
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        global machine_on
        machine_on = False
        return
    elif choice == "report":
        show_resources()
    elif choice == "refill":
        refill()
    else:
        order_ingredients = MENU[choice]["ingredients"]
        if check_resources(order_ingredients):
            total = pay()

            if total < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                return
            else:
                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]

                profit += MENU[choice]["cost"]
                rest = total - MENU[choice]["cost"]
                print(f"Here is ${rest:.2f} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")


while machine_on:
    make_coffee()
