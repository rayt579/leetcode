'''
https://leetcode.com/problems/minimum-window-substring/description/
'''

import collections
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        begin, end = 0, 0
        head = 0
        d = float('inf')
        total = len(t)
        counts = collections.Counter(t)

        while end < len(s):
            if s[end] in counts:
                counts[s[end]] -= 1
                if counts[s[end]] >= 0:
                    total -= 1
            while total == 0:
                if end - begin + 1 < d:
                    d = end - begin + 1
                    head = begin
                if s[begin] in counts:
                    counts[s[begin]] += 1
                    if counts[s[begin]] > 0:
                        total += 1
                begin += 1
            end += 1

        return '' if d == float('inf') else s[head:head+d]

sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABC'))



