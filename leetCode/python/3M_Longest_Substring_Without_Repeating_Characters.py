"""
Problem: 3. Longest Substring Without Repeating Characters (LeetCode, Medium)

Given a string s, find the length of the longest substring without duplicate characters.

-----------------------------------------------------
Examples:

Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without duplicates is "abc" (length 3)

Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without duplicates is "b" (length 1)

Input: s = "pwwkew"
Output: 3
Explanation: The longest substring without duplicates is "wke" (length 3)
Note: "pwke" is not valid since it's a subsequence, not a substring.

-----------------------------------------------------
Constraints:
- 0 <= s.length <= 5 * 10^4
- s may contain English letters, digits, symbols, and spaces

-----------------------------------------------------
Approach:
We use the sliding window technique with two pointers (left and right).
- Maintain a hash map (dictionary) that stores the last index of each character.
- Expand the window by moving the right pointer.
- If a duplicate character is found inside the window, move the left pointer
  just after the last occurrence of that character.
- Update the maximum length at each step.

Time Complexity: O(n), where n = length of string
Space Complexity: O(min(n, charset)), since we store at most one entry per unique character
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
    
# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3