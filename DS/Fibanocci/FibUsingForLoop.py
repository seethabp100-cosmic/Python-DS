#using for loop
a=0
b=1
n = int(input("Enter:: "))
for i in range(n):
    if(i<=n):
        newFib = a+b
        a=b
        b=newFib
        print("Fibanocci:: ",newFib)
    else:
        print("n:: ",n);