#Find permutation of a given string
def toString(list):
    return ''.join(list)

def permutation(string,l,r):
    if l==r:
        print(toString(string))
    else:
        for i in range(l, r+1):
            string[l], string[i] = string[i], string[l]
            permutation(string, l+1, r)
            string[l], string[i] = string[i], string[l]

print(permutation(list('abc') ,0,2))