'''
class area:
    def rectangle(self,l,b):
        return l*b
class square(area):
    def square1(self,b):
        return b*b
class circle(square):
    def circle1(self,b):
        return 3.14*(b**2)
c=circle()
func=int(input("Enter the funtion u want to perform press 1 for rectangle\n press 2 for square\n press 3 for circle"))
if(func==1):
    l=int(input("Enter the length"))
    b=int(input("Enter th breadth"))
    print("Area of rectangle is : ",c.rectangle(l,b))
elif(func==2):
    b=int(input("Enter the si of square"))
    print("area of square is : ",c.square1(b*b))
elif(func==3):
    b=int(input("Enter the radious of the circle"))
    print("area of circle is : ",c.circle1(b))
else:
    print("invalid input")
'''

#patterns of right angle triangle, invert right angle triangle,simple triangle, cone, square
class right_angle:
    def right_triangle(self,n):
        print("The pattern is ")
        r=1
        while(r<n+1):
            print(" "*(n-r)+"*"*r)
            r=r+1
class triangle(right_angle):
    def triangle1(self,n):
        r=1
        while(r<n+1):
            if r==1:
                print(' '*(n-r)+'*')
            else:
                print(' '*(n-r)+'*'*r+'*'*(r-1))
            r=r+1
            
            
'''
class square(triangle):
    def square1(self,n):
        while(n<0):
            if(n==1 or n==n):
                print("*"*n)
            else:
                print("*"+" "
'''
class hollow(triangle):
    def hollow1(self,n):
        i=1
        while i<=n:
            if i==1:
                print(' '*(n-i)+'*')
            elif i==n:
                print('*'*(2*i-1))
            else:
                print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
            i=i+1
        
c=hollow()


func=int(input("Enter the pattern you want to print: \nFor right angle triangle press 1,\npress 2 for inverted triangle,\n press 3 for simple triangle,\n press 4 for cone,\n press 5 for square"))
if(func==1):
    n=int(input("Enter the rows"))
    c.right_triangle(n)
elif(func==2):
    n=int(input("Enter the rows"))
    c.triangle1(n)
elif(func==3):
    b=int(input("enter the rows: "))
    c.hollow1(b)
