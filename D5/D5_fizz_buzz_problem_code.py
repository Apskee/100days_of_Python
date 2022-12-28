#Goal of this excercise is to print outcome depending on number which is currently being evaluated by a for loop.
#Rules:
#Your program should print each number from 1 to 100 in turn.

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


##### SOLUTION #####

#For loop
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0: #Divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0: #Divisible only by 3
        print("Fizz")
    elif number % 5 == 0: #Divisible only by 5
        print("Buzz")  
    else:
        print(number)


##### EXPLANATION #####
#Created a for loop that checks all conditions as per rules, first condition checked had to be the one checking if divisible by both 3 and 5
#because otherwise it would have been skipped.