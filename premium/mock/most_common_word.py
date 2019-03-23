import re
class Solution:
    def mostCommonWord(self, paragraph, banned) -> str:
        paragraph = re.sub(r'\W+', ' ', paragraph)
        banned = set(banned)

        words = [word.lower() for word in paragraph.split(' ')]
        word_counts = {}
        max_freq_word, most_common_word = 0, None

        for word in words:
            #print('visiting word: {}'.format(word))
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
            if word_counts[word] > max_freq_word and word not in banned:
                max_freq_word = word_counts[word]
                most_common_word = word
        return most_common_word

sol = Solution()
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
banned = ['hit']
paragraph2 = 'Bob. hIt, baLl'
banned2 = ['bob','hit']
print(sol.mostCommonWord(paragraph, banned))
print(sol.mostCommonWord(paragraph2, banned2))
