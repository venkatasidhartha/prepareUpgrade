"""
27. Remove Element
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
"""

def removeElement(nums: list, val: int) -> int:
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k+=1
    return k

# removeElement([3,2,2,3],3)
removeElement([0,1,2,2,3,0,4,2],2)