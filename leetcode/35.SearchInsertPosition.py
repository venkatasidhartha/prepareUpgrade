"""
35. Search Insert Position
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

def searchInsert(nums: list, target: int) -> int:
    for count,i in enumerate(nums):
        if i >= target:
            return count
    return len(nums)

print(searchInsert([1,3,5,6],10))