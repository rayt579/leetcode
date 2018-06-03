'''
https://leetcode.com/problems/sqrtx/description/
'''

import sys
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        lo, hi = 0, 4294967296
        while lo < hi:
            mid = (hi - lo)//2 + lo
            if mid * mid <= x:
                if (mid+1) * (mid+1) > x:
                    return mid
                else:
                    lo = mid
            else:
                hi = mid

        return lo

sol = Solution()
print('Expect 1: {}'.format(sol.mySqrt(1)))
print('Expect 2: {}'.format(sol.mySqrt(4)))
print('Expect 4: {}'.format(sol.mySqrt(16)))
print('Expect 8: {}'.format(sol.mySqrt(64)))
print('Expect 8: {}'.format(sol.mySqrt(74)))


