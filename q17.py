      """
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""


#SOLUTION


def longestSubarray(nums):
    max_length = 0
    current_length = 0
    prev_length = 0
    for num in nums:
        if num == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            prev_length = current_length
            current_length = 0
        max_length = max(max_length, prev_length + current_length)
    return max_length if max_length > 0 else 0

# Test cases
nums1 = [1, 1, 0, 1]
nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
nums3 = [1, 1, 1]

print(longestSubarray(nums1))  # Output: 3
print(longestSubarray(nums2))  # Output: 5
print(longestSubarray(nums3))  # Output: 2
