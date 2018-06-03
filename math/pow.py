'''
https://leetcode.com/problems/powx-n/description/
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1/x

        result = 1
        while n != 0:
            if n % 2 == 0:
                x *= x
            else:
                result *= x
                x *= x

            n = n // 2

        return result



sol = Solution()
print(sol.myPow(2.5, -5))
