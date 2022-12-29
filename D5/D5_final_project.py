#Goal of this final project is to create a password generator

##### SOLUTION #####

#Importing library
import random

#Lists with all characters needed
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Asking user for input on how many letter, symbols and numbers is needed.
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Random letters
password = [] #Empty variable for storing password

#For loop to generate letters
for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))

#Random symbols
#For loop to generate symbols
for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

#Random numbers
#For loop to generate numbers
for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

#Shuffling list "password"
random.shuffle(password)

#Converting list into a string
password = "".join(password)

#Printing outcome
print(password)


##### EXPLANATION #####
#First I imported a library in order to be able to use random functions
#Declared lists with characters I use to generate a password
#Asked user for input to find out how many characters need to be used
#Created for loops for random numbers, symbols and letters which I stored into a list
#Shuffled the list to make it completely random
#Printed the outcome