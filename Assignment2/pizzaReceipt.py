# Name: Eunsung Kim
# Program Description: The program contains a function for creating a receipt
# based on the pizza order received from the user. The function converts a
# list received from order.py into a receipt.

# Function for generating receipt
def generateReceipt(pizzaOrder):
    # If the list is empty
    if not pizzaOrder:
        print("You did not order anything")
        # end the function
        return

    # Receipt
    print("Your order:")
    totalCost = 0
    TAX_RATE = 0.13
    # Repeat the process for each pizza order
    for i in range(len(pizzaOrder)):
        size = pizzaOrder[i][0]
        # Set the cost and topping cost depending on the pizza size
        if size == "S":
            cost = 7.99
            adCost = 0.50
        elif size == "M":
            cost = 9.99
            adCost = 0.75
        elif size == "L":
            cost = 11.99
            adCost = 1.00
        elif size == "XL":
            cost = 13.99
            adCost = 1.25
        else:
            print("Invalid Size")
            return
        print("Pizza %d: %-10s %15.2f" % (i + 1, size, cost))
        totalCost += cost
        toppings = pizzaOrder[i][1]
        # Repeat for each topping
        for j in range(len(toppings)):
            print("- %s" % toppings[j])
        # If there are more than 3 toppings, add the extra topping cost
        for k in range(len(toppings) - 3):
            print("Extra Topping %-10s %10.2f" % ("(" + size + ")", adCost))
            totalCost += adCost
    # Calculate tax by multiplying the cost by the tax rate
    tax = totalCost * TAX_RATE
    # Output tax and total cost
    print("%-20s %14.2f" % ("Tax:", tax))
    print("%-20s %14.2f" % ("Total: ", totalCost + tax))
