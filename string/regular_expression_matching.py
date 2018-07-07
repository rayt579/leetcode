'''
https://leetcode.com/problems/regular-expression-matching/description/
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match_pure_bottom_up(s, p)

    def is_match_topdown_memoize(self, s, p):
        is_match = {}
        def helper(i, j):
            positions = (i, j)
            if positions in is_match:
                return is_match[positions]

            if j >= len(p):
                res = i >= len(s)
            else:
                first_match = i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    res = helper(i, j+2) or first_match and helper(i+1, j)
                else:
                    res = first_match and helper(i+1, j+1)

            is_match[positions] = res
            return res

        helper(0, 0)
        return is_match[(0,0)]

    def is_match_bottom_up(self, s, p):
        is_match = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        is_match[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.')
                if j + 1 < len(p) and p[j+1] == '*':
                    is_match[i][j] = is_match[i][j+2] or first_match and is_match[i+1][j]
                else:
                    is_match[i][j] = first_match and is_match[i+1][j+1]
        return is_match[0][0]

    def is_match_pure_bottom_up(self, s, p):
        is_match = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        is_match[0][0] = True

        for i in range(len(p)):
            if p[i] == '*' and i > 0:
                is_match[0][i+1] = is_match[0][i - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    is_match[i+1][j+1] = is_match[i][j]
                elif p[j] == '*':
                    if s[i] != p[j - 1] and p[j-1] != '.':
                        is_match[i+1][j+1] = is_match[i+1][j-1]
                    else:
                        is_match[i+1][j+1] = is_match[i+1][j] or is_match[i+1][j-1] or is_match[i][j+1]
        return is_match[len(s)][len(p)]


sol = Solution()
print('Expect True: {}'.format(sol.isMatch('aa','a*')))
print('Expect True: {}'.format(sol.isMatch('aa','.*')))
print('Expect False: {}'.format(sol.isMatch('ab','a*')))
print('Expect True: {}'.format(sol.isMatch('aab','c*a*b')))
print('Expect True: {}'.format(sol.isMatch('aa', 'a*')))
print('Expect False: {}'.format(sol.isMatch('ab', '.*c')))
print('Expect True: {}'.format(sol.isMatch('', '.*')))
print('Expect True: {}'.format(sol.isMatch('aab', 'a*a*a*b')))
