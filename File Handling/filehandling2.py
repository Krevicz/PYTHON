file1 = open('text2.txt', 
             'r')
file2 = open('text.txt',  'w')

#reading each line from original
#text file
for line in file1.readlines(): 
    
    #reading all lines that do not
    #begin with "Coding"
    if not (line.startswith('Coding')):
        
        #printing those lines
        print(line)
        
    #storing only those lines that
    #do not begin with "Coding"
    file2.write(line)
    
#close and save the files
file2.close()
file1.close()