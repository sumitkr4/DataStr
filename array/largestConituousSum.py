def largestContinuousSum(arr):
    # ##1st Method
    # maxtillnow=0
    # max_sum=arr[0]
    # for n in arr:
    #     if maxtillnow<0:
    #         maxtillnow=0
    #     maxtillnow+=n
    #     max_sum=max(maxtillnow,max_sum)
    # return max_sum
    ##2nd Method
    if len(arr)<=0:
        return 0
    current_sum=max_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
    return max_sum

arr=[1,2,-1,3,4,10,10,-10,1]
print(largestContinuousSum(arr))

