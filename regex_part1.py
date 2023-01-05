'''import re
str="Saurabh is 22 and Ravi is 34 and Sonam is 33"
age=re.findall(r'\d{1,3}',str)
print(age)
names=re.findall(r'[A-Z][a-z]*',str)
print(names)

agedict={}

x=0
for i in names:
     agedict[i]=age[x]   #dict_name[key_name]=value_name[value]
     x+=1
print(agedict)
'''
import re
str="Welcome to python class. class is in kalkaji"

a=re.findall(r'[a-z]*',str)
print(a)





'''


str=Alter Table
Sometimes, we may forget to create some columns,
or we may need to update the table schemes.
The alter statement used to alter the table schemes if required.
Here, we will add the column branch_name to the table Employee.
The following SQL query is used for this purpose.schemes Schemes

#search,findall,finditer

a=re.findall('alter',str)

for i in a:
    print(i)


a=re.finditer('schemes',str)

for i in a:
    print(i)
'''






















