#Goal of this project is to simply ask for input from a user and then switch the variables

#Asking for input
n1 = input("number1: ")
n2 = input("number2: ")
print(n1)
print(n2)

##### SOLUTION #####
temp = n1
n1 = n2
n2 = temp

#printing outcome
print(n1)
print(n2)


##### Explanation #####
#In order to switch the variables, a new, temporary variable had to be created in order to store variable n1, which then could be assigned to varbiable n2