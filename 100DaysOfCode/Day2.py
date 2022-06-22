# Tip Calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
x = 1
if tip == 12:
    x = 1.12
elif tip == 10:
    x = 1.1
elif tip == 15:
    x = 1.15
people = int(input("How many people to split the bill between? "))
print("Each person should pay: $" + "{:.2f}".format(total_bill/people*x))
