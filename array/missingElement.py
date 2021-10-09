def missingNumber(arr1,arr2):
     ## 1st Method
     # s1=sum(arr1)
     # s2=sum(arr2)
     # result = s1-s2
     # return result

     ##2nd Method
     # for item in arr1:
     #     if item not in arr2:
     #         return item
     ## 3rd Approach
     # arr2.sort()
     # arr1.sort()
     # for num1,num2 in zip(arr1,arr2):
     #     if num1!=num2:
     #         return num1
     ## 4th Approach
     result =0
     for num in arr1+arr2:
         result ^= num
         print(result)
     return result


print(missingNumber([1,2,3,4,5,6,7,8],[3,7,2,1,4,6,8]))