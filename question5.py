# Question 5
a= int(input("Enter the number of rows you want: "))
ascii_no=65
for i in range(0,a):
    for j in range(0,i+1):
        b=chr(ascii_no)
        print(b,end="")
        ascii_no+=1
        if ascii_no>90:
            ascii_no=65
    print("")