'''
https://leetcode.com/problems/reverse-bits/description/
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(32):
            m = m << 1 & 0xFFFFFFFF
            m = m | (n & 1) & 0xFFFFFFFF
            n = n >> 1 & 0xFFFFFFFF
        return m

sol = Solution()
print('Expecting 964176192: {}'.format(sol.reverseBits(43261596)))
