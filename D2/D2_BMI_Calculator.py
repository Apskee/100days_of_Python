#Goal is to calculate person's BMI bases on their input and print it out as a whole number
weight = input("What is your weight? ")
height = input("What is your height? ")

##### SOLUTION ##### 
height = float(height) ** 2
weight = float(weight)
bmi = weight / height
bmi_whole_number = int(bmi)

#Printing the outcome
print(bmi_whole_number)


##### EXPLANATION #####
# BMI = kg/m2, in order to make this division I had to convert the string into a floating number, then raise height to the power of 2 and finally make the calculation, 
# convert it to an integer so I can print it as a whole number.