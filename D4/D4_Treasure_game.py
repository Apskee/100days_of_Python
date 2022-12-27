#Goal of this excercise is to place a marker "X" on a location user chooses by using input
#Creating lists, nesting list and asking user for input
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


##### SOLUTION 1 #####
#Converting input into an integer
choice = int(position)
#Position for first column
if choice == 11:
    map[0][0] = "X"
elif choice == 12:
    map[1][0] = "X"
elif choice == 13:
    map[2][0] = "X"
#Position for second column
if choice == 21:
    map[0][1] = "X"
elif choice == 22:
    map[1][1] = "X"
elif choice == 23:
    map[2][1] = "X"
#Position for third column
if choice == 31:
    map[0][2] = "X"
elif choice == 32:
    map[1][2] = "X"
elif choice == 33:
    map[2][2] = "X"


##### SOLUTION 2 #####
#horizontal = int(position[0])
#vertical = int(position[1])

#map[vertical - 1][horizontal - 1] = "X"


##### EXPLANATION #####
#First I had to convert user's input into an integer and then simply create if statements to determine where the marker "X" goes per user's choice.
