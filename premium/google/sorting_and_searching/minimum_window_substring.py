'''
https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/345/
'''

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            return ''

        min_length, min_i, = float('inf'), float('inf')
        t_counts, remaining = Counter(t), len(t)
        i = 0

        for j in range(len(s)):
            if s[j] in t_counts:
                t_counts[s[j]] -= 1
                if t_counts[s[j]] >= 0:
                    remaining -= 1
                while remaining == 0:
                    length = j - i + 1
                    if length < min_length:
                        min_length, min_i = length, i
                    if s[i] in t_counts:
                        t_counts[s[i]] += 1
                        if t_counts[s[i]] == 1:
                            remaining += 1
                    i += 1

        return '' if min_length == float('inf') else s[min_i:min_i + min_length]

sol = Solution()
res = sol.minWindow('ADOBECODEBANC', 'ABC')
print(res)
