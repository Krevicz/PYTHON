#Time and Space Complexity
def fun(n):
    return (n*(n+1))/2
print(fun(5))
#It takes one iteration to get the result using the above code
def fun2(b):
    sum = 0
    for i in range(1, b+1):
        sum+=i
    print("sum: ", sum)
fun2(6)
#It takes five iterations to get the result using the above code

#The Time Complexity is low for the first function ad high for the second function

#The Space Complexity is low for the first function and high for second function
