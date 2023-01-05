#operator overloading
'''
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "[{0},{1}]".format(self.x,self.y)
    def __add__(self, other):
        x=self.x//other.x
        y=self.y//other.y
        return Point(x,y)
p1=Point(2,3)
p2=Point(5,6)
p3=p1+p2
print(p3)
print(type(p3))
'''
'''
#programme to find exponent of a no. using operator overloading

class Exp:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __pow__(self,b):
        x=self.x**b.x
        y=self.y**b.y
        return Exp(x,y)
p1=Exp(2,4)
p2=Exp(3,2)
print(p1**p2)'''

'''#less than
class Exp:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __le__(self,b):
        x=(self.x**2)+(self.y**2)
        y=(b.x**2)+(b.y**2)
        return x<=y
p1=Exp(2,4)
p2=Exp(13,7)
print(p1<=p2)
print(p2<=p1)'''
#greater than equal to(ge), not equal to(ne), modulus,multiplication
#polymorphism
'''class A:
    def A1(self):
        print("A1")
    def A2(self):
        print("A2")
class B:
    def A1(self):
        print("B1")
    def A2(self):
        print("B2")
def func(obj):
    obj.A1()
    obj.A2()
x=A()
y=B()
func(x)
func(y)
'''
#Encapsul

class Base:
    def __init__(self):
        self._a=2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print('calling')
        print(self._a)
obj1=Derived()
print(obj1._a)
obj2=Base()
print(obj2._a)
'''

class Base:
    def __init__(self):
        self.a='hello'
        self.__c='hii' #private variable with double underscore
class derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling")
        print(self.__a)
obj1=Base()

obj2=derived()
'''











      
