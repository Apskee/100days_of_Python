#Goal of this project is to create a program that will shift the message user types in by shifting the alphabet inputted number of times to the right


##### SOLUTION #####
#Defining list with letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
#Function to either encode or decode message per user's request
def ceaser(plain_text, plain_shift, plain_direction):
    text = "" #Empty variable storing text after the for loop runs
    for char in plain_text: #For loop, looping through each letter of a word chosen by user
        if char in alphabet: #If user chooses symbol or number other than letters in alphabet
            position = alphabet.index(char) #Getting index of specific letter in chosen word
            if direction == "encode": #If encode is chosen
                new_position = position + shift #Shifting position of that letter by adding shift amount chosen
            else: #If decode is chosen
                new_position = position - shift #Shifting position of that letter by substracting shift amount chosen
            new_letter = alphabet[new_position] #Getting new letter from alphabet
            text += new_letter #Concateneting strings into emtpy variable
        else: #If user chooses symbol or number other than letters in alphabet
            text += char #Simply concatanate string into text without shifting
    print(f"You {plain_direction}d message is {text}")

go_again = True
while go_again:

    #Asking user for input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #Whether to encode or decode
    text = input("Type your message:\n").lower() #What is the message
    shift = int(input("Type the shift number:\n")) #By how many times should the message be shifted to the right
    shift = shift % 26 #If user chooses higher number than there is letter in alphabet   

    ceaser(text, shift, direction)        

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower
    if restart == "no":
        go_again = False
        print("Goodbye")
    
