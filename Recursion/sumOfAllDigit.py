# Given an integer, create a function which returns the sum of all the individual digits in that integer.
# For example: if n = 4321, return 4+3+2+1

def sumOfDigit(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (n%10) + sumOfDigit(n//10)

print(sumOfDigit(23401987))

