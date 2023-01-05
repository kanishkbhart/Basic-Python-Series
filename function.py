'''def add(): #define
    print("add")
add() #calling
'''
'''def add(name):
    print("hello",name)
name=input("enter the name")
add(name)'''


# sum of two inputs using a function

'''def add(a,b):
    return a+b
a=int(input("enter the first no. \n"))
b=int(input("Enter the second no. \n"))
print("addition is: ",add(a,b))'''

#WAP to make a calculator with the help of functn and control statement by user input
a=int(input("Enter the first no. \n"))
b=int(input("enter the second no. \n"))

print("Enter the choice\n1.Addition\n2.subtraction\n3.multiply\n4.division\n5.remainder\n")
f=int(input("enter the choice: "))






def add(a,b):
    return a+b


def sub(a,b):
    c=a-b
    print("subtraction is ",c)


def div(a,b):
    c=a/b
    print("the quotient is",c)


def rem(a,b):
    c=a%b
    print("The remainder is",c)
    


def mul(a,b):
    c=a*b
    return c


if(f==1):
    print("addition is ",add(a,b))
elif(f==2):
    sub(a,b)
elif(f==3):
    print("multiplication is %d"%mul(a,b))
elif(f==4):
   div(a,b)
elif(f==5):
    rem(a,b)
else:
    print("invalid")

