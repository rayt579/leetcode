class TrieNode:
    def __init__(self, label):
        self.label = label
        self.children = [None] * 26
        self.word = None
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('root')

    def build(self, words):
        for word in words:
            curr = self.root
            for ch in word:
                ch_idx = ord(ch) - ord('a')
                if not curr.children[ch_idx]:
                    curr.children[ch_idx] = TrieNode(ch)
                curr = curr.children[ch_idx]
            
            curr.word = word
            curr.end_of_word = True

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        found = set()
        trie = Trie()
        trie.build(words)

        for child in trie.root.children:
            if child:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == child.label:
                            self.dfs(child, board, i, j, found)
        return list(found)

    def dfs(self, curr, board, i, j, found):
        if curr.end_of_word:
            found.add(curr.word)

        c = board[i][j]
        board[i][j] = '#'

        for a, b in [[-1,0],[1,0],[0,-1],[0,1]]:
            x, y = a + i, b + j
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != '#':
                ch_idx = ord(board[x][y]) - ord('a')
                if curr.children[ch_idx]:
                    self.dfs(curr.children[ch_idx], board, x, y, found)
        
        board[i][j] = c

sol = Solution()
board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
res = sol.findWords(board, ['oath', 'pea', 'eat', 'rain'])

board2 = [["a","b"],["a","a"]]
words2 = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
res2 = sol.findWords(board2, words2)

print('Expecting [\'oath\', \'eat\']: {}'.format(res))
print('Expecting [\'aaa\', \'aaab\', \'aaba\',\'aba\',\'baa\']: {}'.format(res2))
