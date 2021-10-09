def sort012(arr):
    ###One method is using 3 loop for each 0 1s and 2s when we get 0/1/2 we will append accordengly

    ###  2nd Method  in one traversal####
    l0=0
    mid=0
    high=len(arr)-1

    while mid<=high:

        if arr[mid] == 0:
            arr[mid], arr[l0] = arr[l0], arr[mid]
            mid += 1
            l0 += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
arr=[0,0,1,2,1,2,0,0,0,0,2,2,0]
sort012(arr)
print(arr)