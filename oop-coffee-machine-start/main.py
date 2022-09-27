from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
while True:
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    choice = input(f"What would you like to drink {menu.get_items()}?: ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if order:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)










