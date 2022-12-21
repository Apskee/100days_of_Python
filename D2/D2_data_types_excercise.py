#User input a 2 digit number, goal is to add the digits of that 2 digit number
two_digit_number = input("Enter a 2 digit number: ")

##### SOLUTION #####
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])

#Printing the outcome
print(first_number + second_number)


##### EXPLANATION #####
#In order to perform addition of 2 digits I had to convert a string variable two_digit_number into an integer and split the 2 digit number into 2 numbers