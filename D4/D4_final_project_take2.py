#ASCI art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pictures = [rock, paper, scissors]
import random
#User choice
choice = int(input("What do you choose, 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(f"You chose{pictures[choice]}")

#PC choice
pc_choice = random.randint(0,2)
print(f"Oponent chose{pictures[pc_choice]}")

#Rules
winning_matrix = [
    ["Its a tie", "You lose", "You win"],
    ["You win", "Its a tie", "You lose"],
    ["You lose", "You win", "Its a tie"]
]

#Printing the outcome
print(winning_matrix[choice][pc_choice])