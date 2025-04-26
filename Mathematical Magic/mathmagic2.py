'''#Check if a number is prime
from math import sqrt

number = int(input("Enter your number : "))
print("\n")

#If a given number is greater than 1
if number > 1:

    #check if number is divisible from 2 to number/2
    for i in range(2, int(sqrt(number))+1):
        
        # if divisibile by any number it is a non prime number
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")
    '''

#SieveOfEratosthenes
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    
    p = 2
    while (p * p <= num):
        
        if (prime[p] == True):
            
            
            for i in range (p * p, num + 1, p):
                prime[i] = False
        p += 1
        
    for p in range(2, num+1):
        if prime[p]:
            print(p)

num = int(input("Enter a number: "))
print("Following are the prime numbers smaller")
print("than or equal to", num)
SieveOfEratosthenes(num)
        