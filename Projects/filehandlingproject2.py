file1 = open('sample.txt', 'r')
file2 = open('sample2.txt', 'w')

for line in file1.readlines():
    
    if not (line.startswith('To')):
        
        print(line)
        
    file2.write(line)
    
file2.close()
file1.close()