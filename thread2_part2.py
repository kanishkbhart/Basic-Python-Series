import threading
import time

exitFlag=0 #for termination
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self) #initialising thread
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("Starting"+self.name)
        print_time(self.name,self.counter,5)
        print("exiting"+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:  #True by default
            threadName.exit()
        time.sleep(delay)  #inbuilt function
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter-=1

#creating new threads
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"thread-2",2)

#Start new threads

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("exiting main thread")
