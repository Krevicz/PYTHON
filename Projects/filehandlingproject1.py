file1 = open('data.txt', 'r')
print(file1.read(5))
print(file1.readlines())
print(file1.readlines())


file2 = open('data1.txt', 'r')
(file2.write("Everyone likes food"))

file1.close()
file2.close()