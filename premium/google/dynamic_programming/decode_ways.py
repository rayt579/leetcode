class Solution:
    def numDecodings(self, s: str) -> int:
        take_single = 1 if '1' <= s[0] <= '9' else 0
        take_pair = 0
        for i in range(1, len(s)):
            num_ways = 0
            if '1' <= s[i] <= '9':
                num_ways += take_single
            if '10' <= s[i - 1 : i + 1] <= '26':
                num_ways += take_pair
            take_pair, take_single = take_single, num_ways
        return take_single

sol = Solution()
res = sol.numDecodings('12')
print('Expect 2: {}'.format(res))
res2 = sol.numDecodings('226')
print('Expect 3: {}'.format(res2))
