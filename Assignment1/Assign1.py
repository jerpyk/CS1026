# Name: Eunsung Kim
# Program Description: The program calculates the inflation rate and type depending
# on the expenses from previous and current years received from the user.

# Receive year of interest from the user
year = int(input("Please enter the year that you want to calculate the personal interest rate for: "))
# Receive the number of expenditure categories
expCat = int(input("Please enter the number of expenditure categories: "))

# expenses for the previous year
prevExp = 0
# expenses for the current year (year of interest)
currExp = 0
# THe number of expenditure categories is the number of times to repeat the loop below
count = expCat

# Repeat until count reaches 0
while count > 0:
    # Find the total previous expenses by adding the received input each time
    prevExp += float(input("Please enter expenses for previous year: "))
    # Find the total current expenses by adding the received input each time
    currExp += float(input("Please enter expenses for year of interest: "))
    # Decrease count by 1 each time
    count -= 1

# Find the inflation rate by using the formula
infRate = (currExp - prevExp) / currExp * 100
# Output the inflation rate for the year of interest with format specifier
print("Personal inflation rate for %d is %.1f%%" % (year, infRate))

# Find the type of inflation depending on the inflation rate
infType = ""
if infRate < 3:
    infType = "Low"
elif 3 <= infRate < 5:
    infType = "Moderate"
elif 5 <= infRate < 10:
    infType = "High"
elif infRate >= 10:
    infType = "Hyper"
# Output the inflation type
print("Type of Inflation:", infType)
