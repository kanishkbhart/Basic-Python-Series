list1=[]
len=int(input("Enter the length of the list: \n"))
for i in range(0,len):
    list1.append(input("Enter the element: "))
number=int(input("Enter a number of your choice as per the operation you want to do on list \n For insert press 1, \n for remove press 2,\n for counting elements press 3, \n for deleting an element press 4 \n for sorting press 5 \n for reverse press 6 \n for displaying index press 7 \n for displayig elements o list press 8  \n"))
def insert1(list1):
    index=int(input("enter index no. \n"))
    object=int(input("enter object to be inserted \n"))
    return list1.insert(index,object)
    
if number==1:
    insert1(list1)
    print(list1)
elif number==2:
    n=int(input("enter the element to be removed \n"))
    list1.remove(n) #remove the elemnt first and then give for print
    print("Final list: ",list1)
elif number==3:
    n=int(input("enter the element to be counted \n"))
    print("Count for the given no. is : ",list1.count(n))
elif number==4:
    n=int(input("Enter the element you want to delet \n")) #takes index as parameter
    del list1[n] #first delete then print
    print("Final list: ",list1)
elif number==5:
    list1.sort() #sort the data first and then print
    print("Sort the data: ",list1)
elif number==6:
    list1.reverse() #reverse the data first and then print
    print("the reverse list is : ", list1)
elif number==7:
    n=int(input("Enter the element of which index is to be found  \n"))
    print("Index of the element is : ",list1.index(n))
elif number==8:
    #to display the list
    Print("Displaying the contents of the list: ")
    for i in list1:
        print(list1[i],end=" ")
else:
    print("Invalid input")
