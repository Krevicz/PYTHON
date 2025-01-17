
file1 = open('text.txt', 'r')
#print(file1.read())
print(file1.read(10))
print(file1.readline())
print(file1.readlines())
file1.close()

'''
file1 = open('text.txt', 'w')
(file1.write('I like to eat KFC.'))
file1.close()

file1 = open('text.txt', 'a')
(file1.write('I like McDonalds'))
file1.close()
'''