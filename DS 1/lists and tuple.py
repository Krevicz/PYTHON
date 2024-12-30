#list
list1 = []
list1.append(1)
list1.append("I love idli")
list1.append("dosa")
list1.append("sambar")
list1.append(7)
list1.append("Chennai")
print(list1)
print("first element", list1[0])
print("last element", list1[-1])
list1.remove("sambar")
print(list1)
print(list1.pop(-2))
list2 = [69, 76, 108, 256, 1008]
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.sort()
print(list2*2)
#tuple
tuple1 = (80, 90, 100, 110, 120)
print(tuple1)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3*3)
tupleNumber = (1,)
tuple3 = tuple3 + tupleNumber
print(tuple3)
print(tuple3[0:3])