
"""
nums = [2,7,11,15], target = 9
"""

nums = [3,2,3]
target = 6
def sum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j]) == target:
                return [i,j]
    return


print(sum(nums=nums,target=target))