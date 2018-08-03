'''
https://leetcode.com/problems/longest-palindromic-substring/description/
'''

class Solution:
    start, max_length = 0, 0

    def longestPalindrome(self, s):
        self.start, self.max_length = 0, 0
        def extend_palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            length = j - i - 1
            if length > self.max_length:
                self.max_length = length
                self.start = i + 1

        if len(s) < 2:
            return s

        for i in range(len(s) - 1):
            extend_palindrome(i, i)
            extend_palindrome(i, i + 1)

        return s[self.start:self.start + self.max_length]


    def longest_palindrome_inefficient(self, s):
        """
        Inefficient because performing a reversal on each substring
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start, max_len = 0, 1
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                if self.is_palindrome(s[i:j]):
                    length = j - i
                    if length > max_len:
                        max_len = length
                        start = i

        return s[start:start + max_len]

    def is_palindrome(self,s):
        return s == s[::-1]

sol = Solution()
print('Expecting bab: {}'.format(sol.longestPalindrome('babad')))
print('Expecting bb: {}'.format(sol.longestPalindrome('cbbd')))
print('Expecting bb: {}'.format(sol.longestPalindrome('bb')))
