'''
https://leetcode.com/explore/interview/card/amazon/84/backtracking/521/
'''
from collections import deque

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.letter_combinations_recursive(digits)

    def letter_combinations_queue(self, digits):
        if not digits:
            return []
        combinations = deque([''])
        digit_to_letters_map = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        for i in range(len(digits)):
            digit = int(digits[i])
            while len(combinations[0]) == i:
                sequence = combinations.popleft()
                for letter in digit_to_letters_map[digit]:
                    combinations.append(sequence + letter)
        return list(combinations)

    def letter_combinations_recursive(self, digits):
        if not digits:
            return []
        digit_to_letters_map = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        combinations = []

        def helper(prefix, i):
            if i == len(digits):
                combinations.append(prefix)
                return
            for letter in digit_to_letters_map[int(digits[i])]:
                helper(prefix + letter, i + 1)

        helper('', 0)
        return combinations




sol = Solution()
print(sol.letterCombinations('23'))
