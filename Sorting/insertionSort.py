def insertionSort(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        hole = i
        while hole>0 and arr[hole-1]>value:
            arr[hole]=arr[hole-1]
            hole=hole-1
        arr[hole]=value

    return arr
arr=[200,23,12,8,8,100,15]
sortedArr = insertionSort(arr)
print(sortedArr)

#In-Place sorting Algorithm
#Time complexity O(n^2)