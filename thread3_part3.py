import threading
lock=threading.Lock()
deposite=100
def add_profit():
    global deposite
    
    #lock.acquire()
    deposite=deposite + 10
    #lock.release()
def pay_bill():
    global deposite
    
    lock.acquire()
    deposite=deposite - 10
    lock.release()
thread1=threading.Thread(target = add_profit, args=())
thread2=threading.Thread(target = pay_bill, args=())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(deposite)
