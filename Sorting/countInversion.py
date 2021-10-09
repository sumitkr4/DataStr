# def countInversion(arr):
#     count=0
    ##### Native solution with time complexity O(n^2) #####
    # for i in range(len(arr)):
    #     for j in range(i,len(arr)):
    #         if arr[i]>arr[j]:
    #             count+=1
    # return count
# arr = [2,4,1,3,5]
# arr=[10,20,30]
# arr=[30,10,5,1]
# print(countInversion(arr))

    #####Optimum solution with time complexity O(nlogn)#####
def mergeSort(arr,n):
    temp_arr = [0]*n
    return _mergeSort(arr,temp_arr,0,n-1)
def _mergeSort(arr,temp_arr,left,right):
    inv_count = 0
    if left < right:
        mid = (left+right)//2
        inv_count+= _mergeSort(arr,temp_arr,left,mid)
        inv_count+= _mergeSort(arr,temp_arr,mid+1,right)
        inv_count+= merge(arr,temp_arr,left,mid,right)
    return inv_count
def merge(arr,temp_arr,left,mid,right):
    i=left
    j=mid+1
    k=left
    inv_count=0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for item in range(left,right+1):
        arr[item] = temp_arr[item]
    return inv_count

arr = [2,4,1,3,5]
n=len(arr)
print(mergeSort(arr,n))


