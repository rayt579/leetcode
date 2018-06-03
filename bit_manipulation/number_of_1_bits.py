'''
https://leetcode.com/problems/number-of-1-bits/description/
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_set_ones = 0
        while n:
            n &= (n - 1)
            count_set_ones += 1
        return count_set_ones

    def hamming_weight_bf(self, n):
        count_set_ones = 0
        while n:
            count_set_ones += n & 1
            n >>= 1
        return count_set_ones

sol = Solution()
print(sol.hamming_weight_bf(11))
print(sol.hammingWeight(11))
