def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n = int(input("Enter a number to find factorial : "))
if(n==0):
    print("Factorial is 1")
else:
    fact = fact(n)
    print(fact)



