"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""

def removeDuplicates(nums: list) -> int:
    k = 0
    for x in nums:
        if k == 0 or x != nums[k-1]:
            nums[k] = x
            k+=1
    return k


removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])