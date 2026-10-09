n = int(input("Enter: "))
def FibFormula(n):
    if(n<1):
        return n
    else:
        fib = FibFormula(n-1)+FibFormula(n-2)
        #print("Fib:: ",fib)
        return fib


print(FibFormula(n))