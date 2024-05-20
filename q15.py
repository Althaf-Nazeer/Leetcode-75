"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

#SOLUTION


def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    
    # Initial vowel count for the first window
    current_vowel_count = sum(1 for char in s[:k] if char in vowels)
    max_vowel_count = current_vowel_count
    
    # Sliding window
    for i in range(k, n):
        if s[i] in vowels:
            current_vowel_count += 1
        if s[i - k] in vowels:
            current_vowel_count -= 1
        max_vowel_count = max(max_vowel_count, current_vowel_count)
    
    return max_vowel_count

# Example usage
print(maxVowels("abciiidef", 3))  # Output: 3
print(maxVowels("aeiou", 2))      # Output: 2
print(maxVowels("leetcode", 3))   # Output: 2
