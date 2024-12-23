workingDays = int(input("Enter the number of working days: "))
absentDays = int(input("Enter the number of absent days: "))
attendancePercentage = ((workingDays - absentDays) / workingDays) * 100
print("Your attendance percentage is: ", attendancePercentage)
if attendancePercentage >= 75:
    print("You are eligible for the exam.")
else:
    print("You are not eligible for the exam.")      