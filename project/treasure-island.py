print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at a crossroad, which way do you want to go?\n Left or Right\n")

if direction == "Left":
  lake = input("You reach a lake, do you want to wait for a boat or swim across?\n Wait or Swim\n")
  
  if lake == "Wait":
    door = input("You have reached a cave with a red       door, blue door and a yellow door. Which door are you     going to open?\n Red, Blue or Yellow\n")
    
    if door == "Blue":
     print("You have found the treasure")
    elif door == "Red":
      print("You have been eaten by beasts. Game Over")
    elif door == "Yello":
      print("You have been burned by fire. Game Over")
    else:
      print("You chose a door that does not exist. Game Over.")
  else:
    print("You were attacked by a trout. Game Over.")
else:
  print("You fell into a hole. Game Over")
