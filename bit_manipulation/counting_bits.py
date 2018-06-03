'''
https://leetcode.com/problems/counting-bits/description/
'''

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counted_bits = [0] * (num + 1)
        for i in range(num + 1):
            counted_bits[i] = counted_bits[i >> 1] + (i & 1)

        return counted_bits

sol = Solution()
print(sol.countBits(31))

