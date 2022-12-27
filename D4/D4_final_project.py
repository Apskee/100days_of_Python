#Goal of this project is to create a rock, paper, scissors game
#ASCI art for rock, paper and scissors
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


##### SOLUTION #####
#Importing library
import random

#Determining choices of user and PC
#User
print("1=rock, 2=paper, 3=scissors")
choice = input("Do you choose 1/2/3 ?: ")
user_choice = int(choice)
#PC
pc_choice = random.randint(1,3)

#Determining who wins, user = rock
if user_choice == 1 and pc_choice == 1:
    print(f"{rock} You chose rock")
    print(f"{rock} Oponent chose rock\n")
    print("Its a tie!")
elif user_choice == 1 and pc_choice == 2:
    print(f"{rock} You chose rock")
    print(f"{paper} Oponent chose paper\n")
    print("Oponent chose paper, paper wins against rock, you lose!")
elif user_choice == 1 and pc_choice == 3:
    print(f"{rock} You chose rock")
    print(f"{scissors} Oponent chose scissors\n")
    print("Oponent chose scissors, rock wins against scissors, you win!")

#Determining who wins, user = paper
if user_choice == 2 and pc_choice == 1:
    print(f"{paper} You chose paper")
    print(f"{rock} Oponent chose rock\n")
    print("Paper wins against rock! You WIN!")
elif user_choice == 2 and pc_choice == 2:
    print(f"{paper} You chose paper")
    print(f"{paper} Oponent chose paper\n")
    print("Its a tie!")
elif user_choice == 2 and pc_choice == 3:
    print(f"{paper} You chose paper")
    print(f"{scissors} Oponent chose scissors\n")
    print("Paper loses against scissors, you lose!")

#Determining who wins, user = scissors
if user_choice == 3 and pc_choice == 1:
    print(f"{scissors} You chose scissors")
    print(f"{rock} Oponent chose rock\n")
    print("Scissors lose against rock! You lose!")
elif user_choice == 3 and pc_choice == 2:
    print(f"{scissors} You chose scissors")
    print(f"{paper} Oponent chose paper\n")
    print("Scissors win against paper! You WIN!")
elif user_choice == 3 and pc_choice == 3:
    print(f"{scissors} You chose scissors")
    print(f"{scissors} Oponent chose scissors\n")
    print("Its a tie!")

