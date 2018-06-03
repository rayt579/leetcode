'''
https://leetcode.com/problems/valid-parentheses/description/
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = {'(':')', '[':']','{':'}'}
        stack = []
        for sym in s:
            if sym in open_brackets:
                stack.append(sym)
            else:
                if len(stack) == 0:
                    return False
                open_sym = stack.pop()
                if sym != open_brackets[open_sym]:
                    return False

        return len(stack) == 0

sol = Solution()
print('Expect true: {}'.format(sol.isValid('()')))
print('Expect true: {}'.format(sol.isValid('()[]{}')))
print('Expect true: {}'.format(sol.isValid('{[]}')))
print('Expect false: {}'.format(sol.isValid('(]')))
print('Expect false: {}'.format(sol.isValid('([)]')))

