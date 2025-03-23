'''
def fact(n):
    print(f"All factors of {n}: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

n = int(input("Enter a number"))
fact(n)
'''

#Armstrong number
number = int(input("Enter a number to check if it is armstrong: "))
result = 0
temp = number
while temp != 0:
    digit = temp % 10
    result = result + digit**3
    temp = temp // 10
if number == result:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")
    
    
