class Solution:
    def __init__(self):
        self.results = None
    def wordBreak(self, s, wordDict):
        self.results = {}
        word_set = set(wordDict)
        def has_word_break(i):
            if i == len(s):
                return True
            if i in self.results:
                return self.results[i]
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set and has_word_break(j):
                    self.results[i] = True
                    return True
            self.results[i] = False
            return False
        return has_word_break(0)

sol = Solution()
print('Expecting False: {}'.format(sol.wordBreak('catsandog', ['cats','and','dog'])))
print('Expecting True: {}'.format(sol.wordBreak('catsanddog', ['cats','and','dog'])))

