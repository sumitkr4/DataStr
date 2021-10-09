def bubbleSort(arr):
    for k in range(len(arr)-1):
        for i in range(len(arr)-k-1):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1] = temp
    return arr


arr=[23,12,8,49,100,15]
sortedArr = bubbleSort(arr)
print(sortedArr)


# Time complexity fo bubble sort is 0(n^2)  ## (BC:O(n)) ##
#It is both In-place sorting