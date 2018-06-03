'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

from collections import OrderedDict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring_chars = OrderedDict()
        max_length = 0
        for char in s:
            if char in longest_substring_chars:
                for stale_key in list(longest_substring_chars):
                    del longest_substring_chars[stale_key]
                    if stale_key == char:
                        break
            longest_substring_chars[char] = 0
            max_length = max(len(longest_substring_chars), max_length)

        return max_length

sol = Solution()
a = 'abcabcbb'
b = 'bbbbb'
c = 'pwwkew'
d = 'aab'
e = 'vdff'

print(sol.lengthOfLongestSubstring(a))
print(sol.lengthOfLongestSubstring(b))
print(sol.lengthOfLongestSubstring(c))
print(sol.lengthOfLongestSubstring(d))
print(sol.lengthOfLongestSubstring(e))


