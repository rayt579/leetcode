'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/522/
'''

class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(lo, hi):
            while lo < hi:
                str[lo], str[hi] = str[hi], str[lo]
                lo += 1
                hi -= 1

        reverse(0, len(str) - 1)
        start = 0
        for i in range(1, len(str)):
            if str[i] == ' ':
                reverse(start, i - 1)
                start = i + 1
            elif i == len(str) - 1:
                reverse(start, i)

sol = Solution()
text = ['t','h', 'e', ' ', 's','k','y',' ', 'i','s',' ', 'b', 'l', 'u', 'e']
print('Before: {}'.format(''.join(text)))
sol.reverseWords(text)
print('After: {}'.format(''.join(text)))
