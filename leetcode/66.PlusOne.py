"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

def plusOne(digits: list) -> list:
    return [int(i) for i in str(int("".join(str(x) for x in digits))+1)]

print(plusOne([1,2,3]))