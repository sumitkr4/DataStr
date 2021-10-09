def partition(arr,low,high):
    i=low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]< pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr=[200,23,12,8,8,100,15,300,1]
n=len(arr)
quickSort(arr,0,n-1)
print(arr)

## Time complexity O(nlogn) in avg cases