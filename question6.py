a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
x=0
while(a<=b):
    count=0
    i=2
    while(i<=a//2):
        if(a%i==0):
            count=count+1
        i=i+1
    if(count==0 and a!=1):
        print(a,"is a prime number")
        x=x+1
    a=a+1
print("Total prime numbers: ",x)
