def intro(name):
    print("Hello, my name is " + name)

user_name = str(input("Enter your name: "))
intro(user_name)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Choose one of the following operations: ")
print("1. Addition 2. Subtraction 3. Multiplication 4. Division")
choice = int(input("Enter your choice: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == 1:
    print(f"The sum of {num1} and {num2} is", add(num1, num2))
elif choice == 2:
    print(f"The difference of {num1} and {num2} is", subtract(num1, num2))
elif choice == 3:
    print(f"The product of {num1} and {num2} is", multiply(num1, num2))
elif choice == 4:
    print(f"The quotient of {num1} and {num2} is", divide(num1, num2))
else:
    print("Invalid choice")