'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/480
'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_freq = Counter(s)
        for i in range(len(s)):
            if s[i] in letter_freq and letter_freq[s[i]] == 1:
                return i
        return -1

sol = Solution()
print('Expect 0: {}'.format(sol.firstUniqChar('leetcode')))
print('Expect 2: {}'.format(sol.firstUniqChar('loveleetcode')))