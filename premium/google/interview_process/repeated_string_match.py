'''
https://leetcode.com/explore/interview/card/google/67/sql-2/469
'''

class Solution:
    def repeatedStringMatch(self, A, B):
        if not A or not B:
            return -1
        count = 0
        sb = []
        while len(sb) < len(B):
            sb.extend(list(A))
            count += 1
        if B in ''.join(sb):
            return count
        sb.extend(list(A))
        count += 1

        return count if B in ''.join(sb) else -1

sol = Solution()
print('Expecting 3: {}'.format(sol.repeatedStringMatch('abcd', 'cdabcdab')))

