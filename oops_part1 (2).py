'''class calculation:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

c=calculation()
print("Sum is: ",c.add(5,4))
print("Subtraction is : ",c.sub(9,5))
class Employee:  
    a=10
    b=20

    def add(self,a,b):
        print(a+b)
  
  
emp1 = Employee()
emp1.add()

'''
'''
# multi level inheritance
class add:
    def add1(self,a,b):
        return a+b
class sub:
    def sub1(self,a,b):
        return a-b
class mul(sub,add):
    def mul1(self,a,b):
        return a*b
a=mul()
a.sub1(2,3)
a.add1(2,3)
'''

#factorial and to find odd and even no.

class fact:
    def fact1(self,a):
        f=1
        for i in range(a,0,-1):
            f=a*f
            a=a-1
            if a==0:
                break
        print("The factorial of the given no. is ",f)

class type:
    def type1(self,a):
        if a%2==0:
            print("no. is even")
        else:
            print("no. is odd")

class op(type,fact):
    pass
    
    
    
n=int(input("enter a no."))
a=op()
a.fact1(n)
a.type1(n)
'''
import math
n=int(input("enter the num: "))
print(math.factorial)'''
            
            
