'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        start, end = 0, 0
        nonrepeats = set()
        while start <= end and end < len(s):
            if s[end] not in nonrepeats:
                nonrepeats.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                nonrepeats.remove(s[start])
                start += 1

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


