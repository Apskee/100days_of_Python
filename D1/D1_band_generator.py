#Goal of this project is to create a name generator for a band depending on user's input

#Printing the welcome message
print("Welcome to the band generator!!")

#Asking user for input, depending on which the name will be generated
city = input("What is the city you grew up in?\n")
pet = input("What is the name of your pet?\n")

#Generating the band name using concatenation
print (city + " " + pet)