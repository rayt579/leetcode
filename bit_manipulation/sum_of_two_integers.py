'''
https://leetcode.com/problems/sum-of-two-integers/description/

Python implements an infinite twos-complement representation
'''

class Solution:

    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        while b:
            carry = a & b
            a = (a^b) & mask
            b = (carry << 1) & mask
        return a if a <= MAX else ~(a ^ mask)

# Case where you can loop infinitely
sol = Solution()
print('Expect -200000: {}'.format(sol.getSum(-100000, -100000)))

