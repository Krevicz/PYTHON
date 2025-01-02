num = 6
while True:
    guess = int(input("Guess the number"))
    if guess == num:
        print("You are correct")
        break
    elif guess < num:
        print("The number is higher")
    elif guess > num:
        print("The number is lower")
    else:
        print("Invalid input")