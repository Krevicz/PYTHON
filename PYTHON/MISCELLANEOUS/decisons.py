answer = int(input("Enter speed?"))
if answer > 263:
    print("New ATP record!")
elif answer <= 263 and answer >= 230:
    print("Top 20")
elif answer < 230:
    print("Keep working on that serve.")