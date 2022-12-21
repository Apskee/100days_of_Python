#Goal of this project is to simply ask for input from a user and then switch the variables

#Asking for input
n1 = input("number1: ")
n2 = input("number2: ")
print(n1)
print(n2)

######## SOLUTION #######
temp = n1
n1 = n2
n2 = temp

#printing outcome
print(n1)
print(n2)