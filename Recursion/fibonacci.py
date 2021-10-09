n=10
cache=[None]*(n+1)
def fibonacci(n):
    # #Iterative way
    # a=0
    # b=1
    # for i in range(n):
    #     a,b=b,a+b
    # return a

    # #Recursive Way
    # if n==0 or n==1:
    #     return n
    # return fibonacci(n-1)+fibonacci(n-2)

    #Dynamically way
    if n==0 or n==1:
        return n
    if cache[n] != None:
        return cache[n]
    cache[n] = fibonacci(n-1)+fibonacci(n-2)
    return cache[n]
print(fibonacci(n))