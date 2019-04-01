import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub('[^A-Za-z0-9]', ' ', paragraph)
        print(paragraph)
        banned = set(banned)
        counts = {}
        highest_count, most_freq_word = float('-inf'), None
        for word in paragraph.split():
            word = word.lower()
            if word in banned:
                continue
            if word not in counts:
                counts[word] = 1
            elif word in counts:
                counts[word] += 1
            if counts[word] > highest_count:
                highest_count = counts[word]
                most_freq_word = word
        return most_freq_word

sol = Solution()
res = sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit', ['hit'])
print('Expecting ball: {}'.format(res))
