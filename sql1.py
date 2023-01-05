'''import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",password="root")
cur=myconn.cursor()
'try:
    cur.execute("show databases")
    
except:
    myconn.rollback()
for i in cur:
    print(i)
myconn.close()'''


#cursor functions

'''import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root",database="Jaijot")
cur=conn.cursor()
sql="insert into student1(rollno,stu_name,school_name) values (%s,%s,%s)"
val=[(105,"saurabh","kps"),(106,"Ankit","kps"),(107,"vikram","kps")]
try:
    cur.executemany(sql,val)
    print(cur.rowcount,"record inserted!")
    conn.commit()
    
except:
    conn.rollback()

conn.close()
'''
'''import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "Jaijot")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Reading the Employee data      
    cur.execute("select * from student1")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
    #printing t
    
      
    for x in result:  
        print(x);  
except:  
    myconn.rollback()  
  
myconn.close()

'''
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root",database="Jaijot")
cur=con.cursor()

try:
    cur.execute("delete from student1 where rollno=107")
    print("delete successfully")
    con.commit()

except:
    con.rollback()

con.close()




















                         
