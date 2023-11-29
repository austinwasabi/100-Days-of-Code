print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay R5.")
    elif age <= 18:
      print("Please pay R7.")
    else:
      print("Please pay R12.")
else:
    print("Sorry, you are too short to ride the rollercoaster.")
