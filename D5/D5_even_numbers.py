#Goal of this excercise is to sum up all even numbers from range 1 to 100

##### SOLUTION #####
#Empty variable to store my calculation
total = 0
#For loop with step value of 2
for number in range(0, 101, 2):
    total += number
#Printing outcome
print(total)


##### EXPLANATION #####
#Created empty variable to store my sum, starting from range 0 I added a step 2 into for loop to only include even numbers.
#Then made the calculation and printed the outcome.