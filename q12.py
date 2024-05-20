"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

#SOLUTION


def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the lines at the two pointers
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        # Update the maximum area if the current area is larger
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(height1))  # Output: 49

height2 = [1,1]
print(maxArea(height2))  # Output: 1
