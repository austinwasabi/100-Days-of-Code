names = names_string.split(", ")

import random
random_postion = random.randint(0, len(names) - 1)
banker = names[random_position]

print(f"{banker} is going to buy the meal today!")
