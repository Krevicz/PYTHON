
num = int(input("Enter a number: "))
num_str = str(num)
sum_of_powers = int(num_str[0]) ** 3 + int(num_str[1]) ** 3 + int(num_str[2]) ** 3
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

