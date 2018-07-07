'''
https://leetcode.com/problems/string-to-integer-atoi/description/
'''
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        negative = False
        i, res = 0, 0

        while i < len(str) and str[i] == ' ':
            i += 1

        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            if str[i] == '-':
                negative = True
            i += 1

        while i < len(str) and ord('0') <= ord(str[i]) <= ord('9'):
            res = res * 10 + ord(str[i]) - ord('0')
            if res < -(2**31) or res > 2 ** 31 - 1:
                return -2**31 if negative else 2**31 - 1
            i += 1

        return res if not negative else -res

sol = Solution()
a = '42'
b = ' -42'
c = '4193 with words'
d = 'words and 987'
e = '-91283472332'
f = '+1'

print('Expect 42: {}'.format(sol.myAtoi(a)))
print('Expect -42: {}'.format(sol.myAtoi(b)))
print('Expect 4193: {}'.format(sol.myAtoi(c)))
print('Expect 0: {}'.format(sol.myAtoi(d)))
print('Expect -214783648: {}'.format(sol.myAtoi(e)))
print('Expect 1: {}'.format(sol.myAtoi(f)))
