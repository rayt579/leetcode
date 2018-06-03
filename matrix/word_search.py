'''
https://leetcode.com/problems/word-search/description/
'''
import collections
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m = len(board)
        n = len(board[0])

        def dfs(i, j, word_index, path):
            if word_index == len(word) - 1:
                return True
            neighbors = [[i+x, j+y] for x, y in directions if 0 <= i+x < m and 0 <= j+y < n]
            for next_i, next_j in neighbors:
                neighbor = (next_i, next_j)
                if neighbor not in path and word[word_index + 1] == board[next_i][next_j]:
                    path.add(neighbor)
                    if dfs(next_i, next_j, word_index + 1, path):
                        return True
            path.remove((i,j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set([(i,j)])):
                        return True
        return False

board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

sol = Solution()
print('Expect True: {}'.format(sol.exist(board, 'ABCCED')))
print('Expect True: {}'.format(sol.exist(board, 'SEE')))
print('Expect False: {}'.format(sol.exist(board, 'ABCB')))

