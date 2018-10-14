from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ''
        
        min_window_len, min_start, min_end = float('inf'), -1, -1
        t_remaining = len(t)
        t_counts = Counter(t)

        start = 0
        for end in range(len(s)):
            if s[end] in t_counts:
                t_counts[s[end]] -= 1
                if t_counts[s[end]] >= 0:
                    t_remaining -= 1
                while start < len(s) and t_remaining == 0:
                    if end - start + 1 < min_window_len:
                        min_window_len = end - start + 1
                        min_start, min_end = start, end
                    if s[start] in t_counts:
                        t_counts[s[start]] += 1
                        if t_counts[s[start]] > 0:
                            t_remaining += 1
                    start += 1

        return '' if min_window_len == float('inf') else s[min_start:min_end+1]

sol = Solution()
print('Expecting BANC: {}'.format(sol.minWindow('ADOBECODEBANC', 'ABC')))
print('Expecting A: {}'.format(sol.minWindow('A', 'A')))
