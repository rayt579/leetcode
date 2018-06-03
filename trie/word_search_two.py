'''
https://leetcode.com/problems/word-search-ii/description/
'''
class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.word = None

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        results = []

        def __build_trie(words):
            root = TrieNode()
            for word in words:
                p = root
                for c in word:
                    if not p.next[ord(c) - ord('a')]:
                        p.next[ord(c) - ord('a')] = TrieNode()
                    p = p.next[ord(c) - ord('a')]
                p.word = word
            return root

        def __dfs(i, j, p):
            if board[i][j] == '#' or p.next[ord(board[i][j]) - ord('a')] == None:
                return

            c = board[i][j]
            p = p.next[ord(board[i][j]) - ord('a')]
            if p.word != None:
                results.append(p.word)
                p.word = None
            board[i][j] = '#'
            if i > 0:
                __dfs(i - 1, j, p)
            if i < len(board) - 1:
                __dfs(i + 1, j, p)
            if j > 0:
                __dfs(i, j - 1, p)
            if j < len(board[0]) - 1:
                __dfs(i, j + 1, p)
            board[i][j] = c

        root = __build_trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                    __dfs(i, j, root)
        return results


def debug_trie(root):
    from collections import deque
    to_visit = deque([root])
    while len(to_visit) > 0:
        node = to_visit.popleft()
        if node.word != None:
            print(node.word)
        for child in node.next:
            if child != None:
                to_visit.append(child)

sol = Solution()
print('Expected   [oath, eat]: {}'.format(sol.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ['oath','pea','eat','rain'])))

print('Expected   [ab, ac, bd, ca, db] : {}'.format(sol.findWords([['a','b'],['c','d']], ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"])))


