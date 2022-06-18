# Question 9
a=input("Enter a string: ")
b=dict()
list1=a.split(' ')
for i in list1:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)