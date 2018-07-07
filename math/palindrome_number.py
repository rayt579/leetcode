'''
https://leetcode.com/problems/palindrome-number/description/
'''
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        res = 0
        while res < x:
            res = 10 * res + (x % 10)
            x = x // 10

        return x == res or x == res//10

    def is_palindrome_using_string(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x = str(x)
        fwd, bwd = 0, len(x) - 1

        while fwd < bwd:
            if x[fwd] != x[bwd]:
                return False
            fwd += 1
            bwd -= 1

        return True

sol = Solution()
a = 121
b = -121
c = 10

print('Expect true: {}'.format(sol.isPalindrome(a)))
print('Expect false: {}'.format(sol.isPalindrome(b)))
print('Expect false: {}'.format(sol.isPalindrome(c)))