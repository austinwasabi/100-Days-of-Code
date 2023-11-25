print("Welcome to Augustine's tip calculator!")
bill = float(input("What was the total bill?\n R"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill + (bill * tip / 100)

print(f"Each person should pay: {round(total_bill / people, 2)}")
