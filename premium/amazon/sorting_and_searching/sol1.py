'''
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/483/
'''

from collections import deque, defaultdict
import string

class Solution:
    def __init__(self):
        self.graph = None
        self.results = None

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        return self.find_ladders(beginWord, endWord, wordList)

    def find_ladders(self, start, end, words):
        if not words:
            return []

        self.results = []
        self.graph = defaultdict(list)
        ladders = {word : float('inf') for word in words}

        queue = deque([start])
        ladders[start] = 0

        while len(queue) > 0:
            word = queue.popleft()
            step = ladders[word] + 1
            for i in range(len(word)):
                builder = list(word)
                for ch in string.ascii_lowercase[:26]:
                    builder[i] = ch
                    new_word = ''.join(builder)
                    if new_word in ladders:
                        if step > ladders[new_word]:
                            continue
                        elif step < ladders[new_word]:
                            queue.append(new_word)
                            ladders[new_word] = step
                        self.graph[new_word].append(word)

        result = deque()
        self.backtrace(end, start, result)

        return self.results

    def backtrace(self, word, start, deck):
        if word == start:
            deck.appendleft(start)
            self.results.append(list(deck))
            deck.popleft()
            return
        deck.appendleft(word)
        if word in self.graph:
            for parent in self.graph[word]:
                self.backtrace(parent, start, deck)
        deck.popleft()

sol = Solution()
print(sol.findLadders('hit', 'cog', ['hot', 'dot', 'dog','lot','log','cog']))
