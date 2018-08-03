'''
https://leetcode.com/problems/integer-to-roman/description/
'''

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        results = []
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L','XL', 'X', 'IX', 'V', 'IV', 'I']

        for i in range(len(values)):
            while num - values[i] >= 0:
                results.append(romans[i])
                num -= values[i]
        return ''.join(results)

sol = Solution()
print('Expecting III: {}'.format(sol.intToRoman(3)))
print('Expecting IV: {}'.format(sol.intToRoman(4)))
print('Expecting IX: {}'.format(sol.intToRoman(9)))
print('Expecting LVIII: {}'.format(sol.intToRoman(58)))
print('Expecting MCMXCIV: {}'.format(sol.intToRoman(1994)))

