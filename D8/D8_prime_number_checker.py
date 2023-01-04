#Goal of this challenge is to determine whether a number is prime or not prime
#Prime number = Divisible only by 1 and itself

##### SOLUTION #####

#Defining a function
def prime_checker(number):
    is_prime = True #Variable that will switch to false if number is not prime
    for i in range(2, number): #For loop to check all options
        if number % i == 0: #If reminder is 0 its not prime
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

#Asking for input and calling a function
n = int(input("Check this number: "))
prime_checker(number=n)