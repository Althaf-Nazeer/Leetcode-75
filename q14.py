"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""


#SOLUTION


def findMaxAverage(nums, k):
    n = len(nums)
    if n < k:
        return 0.0  # If array length is less than k, return 0.0

    # Calculate the sum of the first 'k' elements
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    # The maximum average is the maximum sum divided by k
    return max_sum / k

# Example usage
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
print(f"{findMaxAverage(nums1, k1):.5f}")  # Output: 12.75000

nums2 = [5]
k2 = 1
print(f"{findMaxAverage(nums2, k2):.5f}")  # Output: 5.00000
