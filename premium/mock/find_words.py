class Solution:
    def findWords(self, board, words):
        trie = Trie(words)
        m, n = len(board), len(board[0])
        results = set()
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, set((i, j)), trie.root, results, m, n)
        return list(results)

    def dfs(self, board, i, j, path, curr_node, results, m, n):
        ch_index = ord(board[i][j]) - ord('a')
        if not curr_node.children[ch_index] or (i, j) in path:
            return
        else:
            curr_node = curr_node.children[ch_index]
            # check if end of word reached
            if curr_node.word:
                results.add(curr_node.word)
                return
            else: # not at end of word, visit all neighbors
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        next_point = (x, y)
                        if next_point not in path:
                            path.add(next_point)
                            self.dfs(board, x, y, path, curr_node, results, m, n)
                            path.remove(next_point)


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.word = None
        self.children = [None] * 26

class Trie:
    def __init__(self, words):
        self.root = self.build_trie_from_words(words)

    def build_trie_from_words(self, words):
        root = TrieNode('root')
        for word in words:
            curr = root
            for i, c in enumerate(word):
                ch_i = ord(c) - ord('a')
                if not curr.children[ch_i]:
                    curr.children[ch_i] = TrieNode(c)
                    if i == len(word) - 1:
                        curr.children[ch_i].word = word
                curr = curr.children[ch_i]
        return root

words = ['oath', 'pea', 'eat', 'rain']
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
sol = Solution()
res = sol.findWords(board, words)
print('Expecting eat and oath: {}'.format(res))

board2 = ['a','a']
word2 = 'aaa'
res2 = sol.findWords(board2, word2)
print('Expecting empty: {}'.format(res2))
