menu = int(0)
choosenToppings = ""
order = []
donkMenu = ["Bread", "Meat", "Vegetables"]
balance = int(100)

while menu != 3:
    print("Press 1 to choose toppings\nPress 2 to purchase and end\nPress 3 to end without purchase\n")
    menu = int(input("Make your choice\n"))
    if menu == 1:
        print("You may now choose from the following toppings")
        while choosenToppings != str("stop"):
            for x in donkMenu:
                print(x)
            choosenToppings = str(input("Write stop to end or choose your toppings\n"))
            for x in donkMenu:
                if x == choosenToppings:
                    order.append(choosenToppings)
            if choosenToppings == str("stop"):
                print("You may not choose any more toppings")
            else:
                print("You have not choosen a valid topping, try again")
    elif menu == 2:
        print("This is what you have choosen\n", order)
    elif menu == 3:
        print("You have not made any purchases\nGoodbye")
