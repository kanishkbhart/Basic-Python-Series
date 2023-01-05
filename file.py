'''import file;  
name = input("Enter the name?")  
file.displayMsg(name)  
'''
'''
#read mode
file=open("C:\\Users\\Kanu\\Desktop\\New folder\\jaijot.txt","w")
file.write("Hello jaijot. \n Welcome to python class; Topics: variables, fnctions, loops")
file.close()
'''
'''
#readline function
file=open("C:\\Users\\Kanu\\Desktop\\New folder\\jaijot.txt","r")

for i in file:
    print(i) #to print entire file
display=file.read(15)#indexno.
display2=file.readline()
print(display2)
file.close()
'''
'''
#a mode to append a new string:
file=open("C:\\Users\\Kanu\\Desktop\\New folder\\jaijot.txt","a")
file.write("Welcome welcome welcome.\n hello hello hello")
file.close()
'''
'''
#how to create a new file:
file1=open("C:\\Users\\Kanu\\Desktop\\New folder\\python.txt","x")
print(file1)
if file1:
    print("file created successfully")
file1.close()
'''
'''
#how to rename a file:
import os
os.rename("C:\\Users\\Kanu\\Desktop\\New folder\\python.txt","C:\\Users\\Kanu\\Desktop\\New folder\\pythonclass.txt")
'''
'''
#how to remove a file:
import os
os.remove("C:\\Users\\Kanu\\Desktop\\New folder\\pythonclass.txt")
'''






