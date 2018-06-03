'''
https://leetcode.com/problems/valid-palindrome/description/
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 0:
            return True

        fwd, bwd = 0, len(s) - 1
        while fwd < bwd:
            while fwd < bwd and not self.is_alphanumeric(s[fwd]):
                fwd += 1
            while fwd < bwd and not self.is_alphanumeric(s[bwd]):
                bwd -= 1
            
            if not s[fwd].lower() == s[bwd].lower():
            	return False
            fwd += 1
            bwd -= 1
        return True


    def is_alphanumeric(self, c):
        if not c:
            return False

        c = c.lower()
        if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
            return True
        return False

sol = Solution()
text1 = "A man, a plan, a canal: Panama"
text2 = "race a car"
text3 = "racecar"
text4 = "race     car"
text5 = '.,'
text6 = ''
text7 = '0P'

print('Expect true: {}'.format(sol.isPalindrome(text1)))
print('Expect false: {}'.format(sol.isPalindrome(text2)))
print('Expect true: {}'.format(sol.isPalindrome(text3)))
print('Expect true: {}'.format(sol.isPalindrome(text4)))
print('Expect true: {}'.format(sol.isPalindrome(text5)))
print('Expect true: {}'.format(sol.isPalindrome(text6)))
print('Expect false: {}'.format(sol.isPalindrome(text7)))
