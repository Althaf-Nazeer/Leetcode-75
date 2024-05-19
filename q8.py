"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""





def increasingTriplet(nums):
    # Initialize two variables to hold the smallest and the second smallest numbers
    first = float('inf')
    second = float('inf')
    
    for n in nums:
        if n <= first:
            first = n  # n is the new smallest number
        elif n <= second:
            second = n  # n is the new second smallest number
        else:
            # We found a number greater than both first and second
            return true
    
    # If we exit the loop without returning, there is no such triplet
    return false

# Example usage:
nums1 = [1, 2, 3, 4, 5]
print(increasingTriplet(nums1))  # Output: true

nums2 = [5, 4, 3, 2, 1]
print(increasingTriplet(nums2))  # Output: false

nums3 = [2, 1, 5, 0, 4, 6]
print(increasingTriplet(nums3))  # Output: true
