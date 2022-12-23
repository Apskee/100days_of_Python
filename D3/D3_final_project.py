#Goal of this project is to create a treasure game, where user chooses a path and using if statements I create a short story for user, ultimate goal is to find the treasure.

#Welcome message
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Rules
print("In order to do so, you need to find the correct path which leads you to the treasure!")
print("Be aware ! Choosing a wrong path may lead to an end and you have to start over.")

#Intro
name = input("What is your name?\n")
print(f"Well, {name}, you find yourself in front of a pyramid and are provided with 2 choices. Doors on the left and doors on the right side.\n")

#Game 
doors = input("Do you want to enter the doors on the left side or right side? Left/Right:\n")
if doors == "Left":
    print(" ")
    print("The doors led you to a room which has no more doors, you got off easy this time !")
    step1 = input("Do you want to return or keep searching the room? Return/Search:\n")
    if step1 == "Search":
        print(" ")
        print('''You spent additional hour searching for some hidden doors or clues, you found nothing and frustrated, you leave and backtrack to where you came from.
Now you are at the beggining of the journey again ! Last time you chose Left, this time you go right''')
    else:
        print(" ")
        print("Now you are at the beggining of the journey again ! Last time you chose Left, this time you go right")
else:
    print(" ")
    print("After entering doors on the right side, you find yourself in front of yet another choice you have to make, this time though, you feel like choosing wrong could be the end.")
step2 = input("You see 3 doors, one with the sign of a treasure chest, second with an eagle and the third doors have sign of a skull. Which do you choose? Treasure/Eagle/Skull:\n")
if step2 == "Treasure":
    print(" ")
    print('''Upon entering doors with a treasure symbol, you find yourself in a completely empty room and shortly after you hear a voice coming out of nowhere.
Unknown voice whispers "Did you really thing it would be this easy?" Shortly after the walls start moving towards you with nowhere to run or hide. This is where you die.\n
!!! GAME OVER !!!''')
elif step2 == "Eagle":
    print(" ")
    print('''Upon entering doors with an eagle symbol, you find yourself in a completely empty room and shortly after you hear the sound of wings flapping, but its not just a sound 
of normal wings. Immediately you know, that what is coming is not a normal bird. After a while a gigantic eagle comes from an opening on the ceiling and grabs you with this claws
flies you up and drops you, ultimately killing you.\n
!!! GAME OVER !!!''')
else:
    print('''You chose the doors with a skull symbol on it, confidently you enter a room which is totally empty, after a while voice starts calling your name. You, being as brave
as you are, of course follow the voice. After a while you hit a dead end and the only way through is through the wall. Confused, you reach your hand and try to push it through the wall,
to your surprise it was a illusionary wall and you came through like nothing was there. The unknown voice reveals to be a long lost treasure chest which is full of gold! Voice
reveals that for your bravery of choosing the doors with a skull symbol, it find you worthy of keeping the gold\n
!!! YOU WIN !!!''')




