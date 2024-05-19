"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""




def compress(chars):
    write = 0
    read = 0
    length = len(chars)
    
    while read < length:
        char = chars[read]
        count = 0
        
        # Count the number of occurrences of the current character
        while read < length and chars[read] == char:
            read += 1
            count += 1
        
        # Write the character to the write position
        chars[write] = char
        write += 1
        
        # Write the count to the write position if greater than 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
                
    return write

# Example usage:
chars1 = ["a","a","b","b","c","c","c"]
new_length1 = compress(chars1)
print(new_length1, chars1[:new_length1])  # Output: 6, ["a","2","b","2","c","3"]

chars2 = ["a"]
new_length2 = compress(chars2)
print(new_length2, chars2[:new_length2])  # Output: 1, ["a"]

chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
new_length3 = compress(chars3)
print(new_length3, chars3[:new_length3])  # Output: 4, ["a","b","1","2"]
