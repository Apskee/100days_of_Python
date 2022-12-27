#Goal of this challenge is to determine which name is going to pay the bill using the random function

#Asking user for input
names_string = input("Give me everybody's names, separated by a comma. ")
#Converting string into a list
names = names_string.split(", ")

##### SOLUTION 1 #####
#Importing library
import random

#Calculating how many inputs I have
number = len(names)
#Generating RNG (variable number - 1 because its a list, starting counting from 0)
random_generator = random.randint(0, number - 1)
#Printing outcome
print(names[random_generator] + " is going to pay for the meal")



##### SOLUTION 2 #####

#person_who_pays = names.choice(names)
#print(person_who_pays)


##### EXPLANATION #####
#First I had to ask user for input then convert it into a list, after that I calculated number of items in the list and generated RNG, using which I printed out the outcome
