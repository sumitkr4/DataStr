### Find all pair in the array that is equal to a given sum.

# ## 1st Method time complexity :- O(nlogon)
#
# arr=[1,3,2,10]
# target = 13
# arr.sort()
# l=0
# r=len(arr)-1
# while l<r:
#     result=arr[l]+arr[r]
#     if result>target:
#         r-=1
#     elif result<target:
#         l+=1
#     else:
#         print(arr[l],arr[r])
#         l+=1

## 2nd Method Time Complexity :-  O(n)

def pairSum(arr, k):
    if len(arr)<2:
        return
    seen = set()
    output = set()
    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))
    print(output)


pairSum([1,3,2,2],4)
