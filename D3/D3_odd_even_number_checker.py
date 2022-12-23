#Goal of this exercise is to build a program that checks whether an inputted number is odd or even
number = int(input("What number would you like to check?: "))

##### SOLUTION #####

if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")


##### EXPLANATION #####
#Using the modulo sign I divided the number inputted into number variable if the division has a reminder the number is odd, if it does not its even.