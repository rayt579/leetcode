from collections import defaultdict, deque
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        return self.find_ladders(beginWord, endWord, wordList)

    def find_ladders(self, start, end, word_list):
        words = set(word_list)
        node_neighbors = defaultdict(list)
        distance = {}
        solution = []
        results = []

        words.add(start)
        self.bfs(start, end, words, node_neighbors, distance)
        self.dfs(start, end, node_neighbors, distance, solution, results)
        return results

    def bfs(self, start, end, words, node_neighbors, distance):
        queue = deque([start])
        distance[start] = 0
        while len(queue) > 0:
            print('Enter while')
            count = len(queue)
            found_end = False
            for i in range(count):
                curr = queue.popleft()
                print('Visit: {}'.format(curr))
                curr_dist = distance[curr]
                neighbors = self.get_neighbors(curr, words)
                for neighbor in neighbors:
                    node_neighbors[curr].append(neighbor)
                    if neighbor not in distance:
                        distance[neighbor] = curr_dist + 1
                        if end == neighbor:
                            found_end = True
                        else:
                            queue.append(neighbor)
                if found_end == True:
                    break

    def dfs(self, curr, end, node_neighbors, distance, solution, results):
        solution.append(curr)
        if curr == end:
            results.append(list(solution))
        else:
            for neighbor in node_neighbors[curr]:
                if distance[neighbor] == distance[curr] + 1:
                    self.dfs(neighbor, end, node_neighbors, distance, solution, results)
        solution.pop()

    def get_neighbors(self, curr, words):
        res = []
        chs = list(curr)

        for ch in string.ascii_lowercase[:26]:
            for i in range(len(chs)):
                if chs[i] == ch:
                    continue
                old_ch = chs[i]
                chs[i] = ch
                new_word = ''.join(chs)
                if new_word in words:
                    res.append(new_word)
                chs[i] = old_ch
        return res

sol = Solution()
print(sol.findLadders('hit', 'cog', ['hot', 'dot', 'dog','lot','log','cog']))
