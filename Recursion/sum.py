# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))