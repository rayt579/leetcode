'''
https://leetcode.com/problems/valid-anagram/description/
'''

from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(Counter(s) - Counter(t)) == 0

sol = Solution()
print('Expect true: {}'.format(sol.isAnagram('anagram','nagaram')))
print('Expect false: {}'.format(sol.isAnagram('rat','car')))
