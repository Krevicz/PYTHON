#dictionary
dict1 = {}
dict2 = {"name": "divya",
         "age": "10",
         "home": "Auckland",
}
print(dict2["name"])
dict3 = dict()
print(dict3)
print(dict1)
dict2["job"] = "teacher"
print(dict2["job"])
del dict2["age"]
print(dict2)
print(dict2.pop("job"))
for i in dict2.keys():
    print(i, ":", dict2[i])
#set
set1 = {1, 1, 1, 1, 1, 1, 1}
print(set1)
set2 = {2, 3, 6, 9}
set3 = {2, 9, 10, 13}
print(set2.intersection(set3))
print(set2.union(set3))
print(set2.difference(set3))
print(set3.difference(set2))
set1.add(2)
print(set1)