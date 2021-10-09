#arr=[200,23,12,8,8,100,15]

def mergeSort(arr):
    middle = len(arr)//2
    if len(arr)>1:
        L=arr[:middle]
        R=arr[middle:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        ## cheacking if any data left in L ##
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        ## cheacking if any data left in R ##
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1


arr=[200,23,12,8,8,100,15,300,1]
mergeSort(arr)
print(arr)

## Time complexity O(nlogn) in all cases