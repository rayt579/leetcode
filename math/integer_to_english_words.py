'''
https://leetcode.com/problems/integer-to-english-words/description/
'''

class Solution:
    LESS_THAN_20 = ['','One','Two','Three','Four', 'Five', 'Six','Seven','Eight','Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen','Eighteen','Nineteen']
    TENS = ['', 'Ten', 'Twenty', 'Thirty','Forty','Fifty','Sixty', 'Seventy','Eighty','Ninety']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        words = []
        if num // 1000000000 > 0:
            words.append(self.number_to_words_less_than_thousand(num // 1000000000))
            words.append('Billion')
            num = num % 1000000000
        if num // 1000000 > 0:
            words.append(self.number_to_words_less_than_thousand(num // 1000000))
            words.append('Million')
            num = num % 1000000
        if num // 1000 > 0:
            words.append(self.number_to_words_less_than_thousand(num // 1000))
            words.append('Thousand')
            num = num % 1000

        words.append(self.number_to_words_less_than_thousand(num))
        return ' '.join(' '.join(words).split())


    def number_to_words_less_than_thousand(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.LESS_THAN_20[num]
        if num < 100:
            return self.TENS[num // 10] + ' ' + self.LESS_THAN_20[num % 10]
        else:
            return self.LESS_THAN_20[num // 100] + ' Hundred ' + self.number_to_words_less_than_thousand(num % 100)

sol = Solution()
print(sol.numberToWords(3564246022))
