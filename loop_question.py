#WAP to print all primeno.s b/w 1-n and find sum of all prime no.s
'''
sum=0
lower=int(input("entre the lower range"))
upper=int(input("enter the upper range"))
for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if((num%i)==0):
                break
        else:
            print(num)
            sum=sum+num
print("sum= ",sum)

'''

#WAP to check if a no. is an armstong no. or not



lower=int(input("Enter starting point \n"))
upper=int(input("enter end point \n"))
for i in range(lower,upper+1):
    j=len(str(i))
    sum=0
    n=i
    while(n>0):
       rem=n%10
    
       sum=sum+(rem**j)
       n=n//10
    if(sum==i):
       print(i)

        
    
