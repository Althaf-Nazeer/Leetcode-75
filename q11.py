"""
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

#SOLUTION


def isSubsequence(s, t):
    i, j = 0, 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Example usage
s1 = "abc"
t1 = "ahbgdc"
print(isSubsequence(s1, t1))  # Output: true

s2 = "axc"
t2 = "ahbgdc"
print(isSubsequence(s2, t2))  # Output: false
