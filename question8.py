# Question 8
list1 = []
for i in range(0,10):
    a=int(input("Enter the number: "))
    if a>0:
        print(a,"is a positive number")
    if a<0:
        print(a,"is a negative number")
    if a%2==0:
        print(a,"is an even number")
    if a%2!=0:
        print(a,"is an odd number")
    list1.append(a)
res={}
for i in list1:
    res[i]=list1.count(i)
print(res)