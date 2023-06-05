# Name: Eunsung Kim
# Program Description: The program receives order from the user and using
# the generateReceipt function form pizzaReceipt.py, it outputs a receipt.
import pizzaReceipt  # imported pizzaReceipt class

# Tuple of available pizza toppings
TOPPINGS = ('ONION', 'TOMATO', 'GREEN PEPPER', 'MUSHROOM', 'OLIVE',
            'SPINACH', 'BROCCOLI', 'PINEAPPLE', 'HOT PEPPER', 'PEPPERONI',
            'HAM', 'BACON', 'GROUND BEEF', 'CHICKEN', 'SAUSAGE')
# Empty list for pizza orders to be contained
pizzas = []
# The order number of a pizza
orderNumb = 0
# Receive whether the user wants to order a pizza
choice = input("Do you want to order a pizza? ")
# If they do, start the loop of receiving orders
while choice.upper() not in ("Q", "NO"):
    # Append a list inside the pizzas list
    pizzas.append([])
    # Receive the size of the pizza until a valid input is given
    size = input("Choose a size: S, M, L, or XL: ")
    while size.upper() not in ("S", "M", "L", "XL"):
        size = input("Choose a size: S, M, L, or XL: ")
    # Record the size abbreviation in uppercase
    size = size.upper()
    # Append the size in the first pizza list
    pizzas[orderNumb].append(size)
    # Append a list to contain the toppings
    pizzas[orderNumb].append([])
    print(
        'Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"')
    toppings = input()
    # Repeat until the user types "X"
    while toppings.upper() != "X":
        # If the user input is in the toppings tuple
        if toppings.upper() in TOPPINGS:
            print("Added %s to your pizza" % toppings.upper())
            # Add the topping to the toppings list
            pizzas[orderNumb][1].append(toppings.upper())
        # If the user inputs "LIST"
        elif toppings.upper() == "LIST":
            # Show the list of available toppings
            print(TOPPINGS)
        # If the user inputs an invalid input
        else:
            # Tell that it is an invalid topping
            print("Invalid topping")
        print(
            'Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"')
        toppings = input()
    # Cast each pizza list into a tuple
    pizzas[orderNumb] = tuple(pizzas[orderNumb])
    choice = input("Do you want to continue ordering? ")
    # Increase the order number each pizza order
    orderNumb += 1

print(pizzas)
# Print the receipt using hte generateReceipt function
pizzaReceipt.generateReceipt(pizzas)
