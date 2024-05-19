"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

def productExceptSelf(nums):
    length = len(nums)
    
    # Initialize the left and right arrays
    left = [0] * length
    right = [0] * length
    answer = [0] * length
    
    # Construct the left array
    left[0] = 1
    for i in range(1, length):
        left[i] = nums[i - 1] * left[i - 1]
    
    # Construct the right array
    right[length - 1] = 1
    for i in range(length - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]
    
    # Construct the answer array
    for i in range(length):
        answer[i] = left[i] * right[i]
    
    return answer

# Example usage:
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
