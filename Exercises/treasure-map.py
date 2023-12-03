line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

x_axis = position[0]

if x_axis == "A":
  x_axis = 0
elif x_axis == "B":
  x_axis = 1
else:
  x_axis = 2

map[int(position[1]) - 1][x_axis] = 'X'

print(f"{line1}\n{line2}\n{line3}")
