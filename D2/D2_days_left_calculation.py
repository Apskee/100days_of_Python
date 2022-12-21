#Goal is to calculate how many years users has left until he/she turn 90 using a f-String, depending on their input
age = input("How old are you? ")


##### SOLUTION #####
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

#Priting the outcome
print(f"You have {days_left}, {weeks_left} weeks, and {months_left} months left until you turn 90")


##### EXPLANATION #####
#Starting from how many years users has left I made my way down to how many days using the calculation and printed it out usinf a f-String.