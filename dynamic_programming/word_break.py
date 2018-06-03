'''
https://leetcode.com/problems/word-break/description/
'''

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

sol = Solution()
print('Expect True: {}'.format(sol.wordBreak('leetcode', ['leet','code'])))
print('Expect False: {}'.format(sol.wordBreak('leetcode', ['leet','codef'])))

