#Goal of this excercise is to calculate whether inputted number is a leap year or not
year = int(input("Which year do you want to check? "))


##### SOLUTION #####
if year % 4 == 0:
    print("Leap year.")
elif year % 100 != 0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")

##### SOLUTION 2 #####

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("Not")
    else:
        print("Yes")  
else:
    print("Not")


##### EXPLANATION #####
#Coming from the formula how to calculate a leap year I first checked if the conditions meet the formula if the year if leap.
#If not I used else to print the message its not a leap year.