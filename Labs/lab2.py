age = int(input("Enter your age: "))
if age >= 9:
    height = float(input("Enter your height in cm: "))
    if height > 130:
        print("You may go on this ride!")
    else:
        print("You are too short for this ride.")
else:
    print("You are too young for this ride.")


IDEAL_CREDIT_SCORE = 720

userScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of the house: "))
# >= should be used instead of =>
if userScore >= IDEAL_CREDIT_SCORE:
    downPayment = 0.1 * housePrice
# elif should be used instead of else if
# 600 should be out of the ""
# logical to use the relational operator instead of using and
elif IDEAL_CREDIT_SCORE > userScore > 600:
    downPayment = 0.2 * housePrice
else:
    # indentation is needed after the else
    downPayment = 0.3 * housePrice

print("Your down payment is: ${}".format(downPayment))
