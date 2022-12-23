#Goal of this project is to divide a bill of an amount user enters along with how many people user chooses that will split the bill, 
#leaving 12% tip and round the outcome to 2 decimals
total_bill = float(input("What was the total bill? "))
total_people = int(input("How many people split the bill? "))
total_tip = int(input("How much percent of a tip would you like to give? Options are 10, 12, 15: "))

##### SOLUTION #####

tip_percentage = total_tip / 100
tip_amount = total_bill * tip_percentage
absolute_bill = total_bill + tip_amount
bill_per_person = absolute_bill / total_people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")

##### EXPLANATION #####
#First I needed to convert total bill to a floating point number and total people to an integer, then make the calculation depending how much tip the user wants to leave.
#Lastly round it up to 2 decimal points.