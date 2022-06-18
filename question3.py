# Question 3
a=int(input("Enter the 1st side of triangle: "))
b=int(input("Enter the 2nd side of triangle: "))
c=int(input("Enter the 3rd side of triangle: "))
#Checking if the triangle exists or not
d=max(a,b,c)
e=a+b+c
f=e-d
if(f>d):
    print("Triangle can be formed")
    s=(a+b+c)/2
    area= ((s)*(s-a)*(s-b)*(s-c))**0.5
    print("Area of the triangle: ",area)
else:
    print("Triangle can not be formed")