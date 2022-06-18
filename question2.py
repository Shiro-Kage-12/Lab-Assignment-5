# Question 2
a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
c=int(input("Enter the number to check divisibility with: "))
for i in range(a,b):
    if i%c==0:
        print(i,"is divisible by",c)
    i=i+1
