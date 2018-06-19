'''
https://leetcode.com/problems/palindromic-substrings/description/
'''

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def extend_palindrome(i, j):
            substring_count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                substring_count += 1
                i -= 1
                j += 1
            return substring_count

        res = 0
        for i in range(len(s)):
            res += extend_palindrome(i, i)
            res += extend_palindrome(i, i + 1)
        return res

sol = Solution()
print('Expecting 3: {}'.format(sol.countSubstrings('abc')))
print('Expecting 6: {}'.format(sol.countSubstrings('aaa')))
print('Expect 0: {}'.format(sol.countSubstrings('')))
print('Expect 1: {}'.format(sol.countSubstrings('a')))
