'''
https://leetcode.com/problems/reverse-integer/description/
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_power_of_10 = 9
        negative = False
        if x < 0:
            negative = True
            x = -x

        while max_power_of_10 > 0:
            y = x % (10 ** max_power_of_10)
            if x == y:
                max_power_of_10 -= 1
            else:
                break

        res = 0
        while max_power_of_10 >= 0:
            digit = x % 10
            res += digit * 10 ** max_power_of_10
            max_power_of_10 -= 1
            x = x // 10

        final = res if not negative else -res

        if - (2**31) <= final < 2**31:
            return final
        else:
            return 0


sol = Solution()
print('Expecting 321: {}'.format(sol.reverse(123)))
print('Expecting -321: {}'.format(sol.reverse(-123)))
print('Expecting 12: {}'.format(sol.reverse(210)))
print('Expecting 0: {}'.format(sol.reverse(0)))
print('Expecting 0: {}'.format(sol.reverse(1534236469)))




