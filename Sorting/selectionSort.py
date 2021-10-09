#In-place selection sort algorithm
def selectionSort(arr):
    for i in range(len(arr)-1):
        iMin=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[iMin]:
                iMin = j
        temp = arr[i]
        arr[i] = arr[iMin]
        arr[iMin] = temp
    return  arr
arr=[23,12,8,8,100,15]
sortedArr = selectionSort(arr)
print(sortedArr)

# Time complexity fo selection sort is 0(n^2)
#It is both In-place sorting or not In-place sorting