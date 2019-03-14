class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start, length = 0, len(s)
        for _ in range(rows):
            start += cols
            if s[start % length] == ' ':
                start += 1
            else:
                while start > 0 and s[(start - 1) % length] != ' ':
                    start -= 1
        return start // length

sol = Solution()
res = sol.wordsTyping(['abc','de','f'], 4, 6)
print('Expecting 2: {}'.format(res))
