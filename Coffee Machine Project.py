logo = r'''  ░██████             ░██           ░██████████             ░██████                 ░████     ░████                       
 ░██   ░██                              ░██                ░██   ░██               ░██       ░██                          
░██         ░███████  ░██░████████      ░██     ░███████  ░██         ░███████  ░████████ ░████████  ░███████   ░███████  
░██        ░██    ░██ ░██░██    ░██     ░██    ░██    ░██ ░██        ░██    ░██    ░██       ░██    ░██    ░██ ░██    ░██ 
░██        ░██    ░██ ░██░██    ░██     ░██    ░██    ░██ ░██        ░██    ░██    ░██       ░██    ░█████████ ░█████████ 
 ░██   ░██ ░██    ░██ ░██░██    ░██     ░██    ░██    ░██  ░██   ░██ ░██    ░██    ░██       ░██    ░██        ░██        
  ░██████   ░███████  ░██░██    ░██     ░██     ░███████    ░██████   ░███████     ░██       ░██     ░███████   ░███████  
                                                                                                                          
                                                                                                                          
                                                                                                                          '''
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
profit = 0
coffee_machine = True

def report():
    print(f"water:{resources["water"]}ml")
    print(f"milk:{resources["milk"]}ml")
    print(f"coffee:{resources["coffee"]}g")
    print(f"Money:${profit}")

def calculate():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    Q, D, N, P = map(float, input(f"Please insert the coins:").split())
    Total = round(quarters * Q + dimes * D + nickles * N + pennies * P,2)
    print(f"Total:{Total}")
    return Total

print(logo)
while coffee_machine:
    user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user == "report":
        report()
    elif user == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < 18:
            print("Sorry there is not enough coffee.")
        else:
            paid = calculate()
            if paid < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif paid == MENU["espresso"]["cost"]:
                profit += paid
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso. Enjoy!")
            else:
                change = round(MENU["espresso"]["cost"] - paid,2)
                print(f"Here is ${abs(change)} dollars in change")
                profit += MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print("Here is your espresso. Enjoy!")
    elif user == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water.")
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        else:
            paid = calculate()
            if paid < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif paid == MENU["latte"]["cost"]:
                profit += paid
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                print("Here is your latte. Enjoy!")
            else:
                change = round(MENU["latte"]["cost"] - paid,2)
                print(f"Here is ${abs(change)} dollars in change")
                profit += MENU["latte"]["cost"]
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                print("Here is your latte. Enjoy!")
    elif user == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough water.")
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < 24:
            print("Sorry there is not enough coffee.")
        else:
            paid = calculate()
            if paid < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif paid == MENU["cappuccino"]["cost"]:
                profit += paid
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                print("Here is your cappuccino. Enjoy!")
            else:
                change = round(MENU["cappuccino"]["cost"] - paid,2)
                print(f"Here is ${abs(change)} dollars in change")
                profit += MENU["cappuccino"]["cost"]
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                print("Here is your cappuccino. Enjoy!")
    elif user == "off":
        coffee_machine = False
