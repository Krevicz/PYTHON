#create a new file
'''
new_file = open('New_File.txt', 'x')
new_file.close()
'''
#check if a file exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("New_file.txt"):
    os.remove("New_file.txt")
else:
    print("The file does not exist.")

'''
os.mkdir("sample")
'''
os.rmdir("sample")