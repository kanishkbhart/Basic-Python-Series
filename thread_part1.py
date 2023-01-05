# thread is a seperate flow of execution.
from threading import*
#thread_object=Thread(target=func_name, args=[arg1........])
'''def disp():
    for i in range(5):
        
        print("thread run")
t=Thread(target=disp)
t.start()
for i in range(5):
    print("main thread")'''
'''class mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a=a
t=mythread(10)
print(t)'''
'''
1. start()
2. run()
3. join()
'''
'''class T(Thread):
    def run(self):
        for i in range(5):
            print("run method")
t=T()
t.start()
t.join()
for i in range(5):
    print("main thread")
'''
#set and get thread name
'''
1.current_thread()
2.getName()
3. setName()
4.name property
'''
'''
def T():
    print("child thread",current_thread().getName())
    current_thread().setName('pankaj')
    print("child thread",current_thread().getName())
t=Thread(target=T)

t.start()
t.join()

print("main thread", current_thread().getName())



'''
'''
def T():
    print("child thread",current_thread().name)
    current_thread().name='pankaj'
    print("child thread",current_thread().name)
t=Thread(target=T)

t.start()
t.join()

print("main thread", current_thread().name)
'''

class hotel:
    def __init__(self, t):
        self.t=t
    def food(self):
        for i in range(1,6):
            print(self.t,i)
h1=hotel('take order from table')
h2=hotel('serve order to table')
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
a=t1.isAlive()
print("a is : ",a)
t1.join()
t2.start()















































        
