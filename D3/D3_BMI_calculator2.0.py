#Goal of this excercise is to calculate BMI depending on users input and then using conditions provide user with information depending on their input and round the number.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

##### SOLUTION #####
#Calcualting the BMI formula.
bmi = round((weight / height ** 2))
#Conditions to determine user's BMI depending on inputted values.
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


##### EXPLANATION #####
#First step was to calculate BMI then using if statements provide user with information about their weight.