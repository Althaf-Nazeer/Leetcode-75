 """
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


#SOLUTION

def moveZeroes(nums):
    lastNonZeroFoundAt = 0

    # Move all the non-zero elements to the front
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[lastNonZeroFoundAt], nums[current] = nums[current], nums[lastNonZeroFoundAt]
            lastNonZeroFoundAt += 1

# Example usage
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]
