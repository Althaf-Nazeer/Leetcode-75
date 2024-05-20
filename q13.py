"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


#SOLUTION


def maxOperations(nums, k):
    num_count = {}
    operations = 0

    for num in nums:
        complement = k - num
        if complement in num_count and num_count[complement] > 0:
            operations += 1
            num_count[complement] -= 1
        else:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
    
    return operations

# Example usage
nums1 = [1, 2, 3, 4]
k1 = 5
print(maxOperations(nums1, k1))  # Output: 2

nums2 = [3, 1, 3, 4, 3]
k2 = 6
print(maxOperations(nums2, k2))  # Output: 1
