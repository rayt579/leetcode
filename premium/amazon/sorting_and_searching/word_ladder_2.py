from collections import deque, defaultdict
import string

class Solution:
    def get_neighbors(self, word, words):
        neighbors = []
        for i in range(len(word)):
            word_arr = list(word)
            for ch in string.ascii_lowercase:
                word_arr[i] = ch
                new_word = ''.join(word_arr)
                if new_word in words and new_word != word:
                    neighbors.append(new_word)
        return neighbors

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words = set(wordList)
        graph = defaultdict(list)
        distance = {}
        shortest_path, results = [], []

        def bfs(start, end):
            explore = deque([start])
            distance[start] = 0
            found_end = False
            while len(explore) > 0:
                if found_end == True:
                    break
                for i in range(len(explore)):
                    word = explore.popleft()
                    curr_dist = distance[word]
                    for next_word in self.get_neighbors(word, words):
                        graph[word].append(next_word)
                        if next_word == end:
                            found_end = True
                            distance[next_word] = curr_dist + 1
                            break
                        if next_word not in distance:
                            distance[next_word] = curr_dist + 1
                            explore.append(next_word)

        def dfs(start, end, path, res):
            path.append(start)
            if start == end:
                res.append(list(path))
            else:
                for next_word in graph[start]:
                    if distance[next_word] == distance[start] + 1:
                        dfs(next_word, end, path, res)
            path.pop()

        bfs(beginWord, endWord)
        dfs(beginWord, endWord, shortest_path, results)
        return results

sol = Solution()
print(sol.findLadders('hit', 'cog', ['hot', 'dot','dog','lot','log','cog']))
print(sol.findLadders('a', 'c', ['a', 'b','c']))
