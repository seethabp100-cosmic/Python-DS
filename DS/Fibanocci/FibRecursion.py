#using recursion
count =0
n = int(input("Enter n:: "))
def fibRecursion(a,b):
    global count
    if(count<n):
        recurFib = a+b
        print("count: ",count, " fib: ",recurFib)
        a=b
        b=recurFib
        count+=1
        fibRecursion(a,b)
    else:
        return
fibRecursion(0,1)
        