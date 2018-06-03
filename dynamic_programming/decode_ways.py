'''
https://leetcode.com/problems/decode-ways/description/
'''

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        n = len(s)
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            if '0' < s[i-1] <= '9':
                res[i] += res[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
                res[i] += res[i - 2]
        return res[n]


    def num_decodings_recursive(self, s):
        n = len(s)
        num_decodings = {}

        def dfs(i):
            if i in num_decodings:
                return num_decodings[i]
            if i == n:
                num_decodings[i] = 1
                return 1
            if s[i] == '0':
                num_decodings[i] = 0
                return 0

            res = dfs(i + 1)
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                res += dfs(i + 2)
            if res not in num_decodings:
                num_decodings[i] = res
            return res

        return 1 if n == 0 else dfs(0)

sol = Solution()
print('Expect 2: {}'.format(sol.numDecodings('12')))
print('Expect 3: {}'.format(sol.numDecodings('226')))
print('Expect 0: {}'.format(sol.numDecodings('0')))
print('Expect 0: {}'.format(sol.numDecodings('226140')))
print('Expect 1: {}'.format(sol.numDecodings('10')))
print('Expect 1: {}'.format(sol.numDecodings('110')))
