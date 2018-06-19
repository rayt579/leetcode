'''
https://leetcode.com/problems/unique-paths/description/
'''
class Solution:
    def uniquePaths(self, m, n):
        score = [[0] * m] * n
        score[n - 1][m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                score_right = score[i][j + 1] if j + 1 < m else 0
                score_bottom = score[i + 1][j] if i + 1 < n else 0
                score[i][j] = score_right + score_bottom

        return score[0][0]

    def unique_paths_recursive_memo(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num_paths_at = {}
        def num_paths(i, j):
            point = (i, j)
            if point in num_paths_at:
                return num_paths_at[point]

            if i == n - 1 and j == m - 1:
                num_paths_at[point] = 1
                return 1

            num_paths_down, num_paths_right = 0, 0
            if i + 1 < n:
                num_paths_down = num_paths(i + 1, j)
            if j + 1 < m:
                num_paths_right = num_paths(i, j + 1)

            num_paths_at[point] = num_paths_down + num_paths_right
            return num_paths_down + num_paths_right

        return num_paths(0, 0)

input1 = [3, 2]
input2 = [7, 3]
sol = Solution()
print('Expecting 3: {}'.format(sol.uniquePaths(input1[0], input1[1])))
print('Expecting 28: {}'.format(sol.uniquePaths(input2[0], input2[1])))

edge1 = [2, 1]
edge2 = [1, 2]
print('Expecting 1: {}'.format(sol.uniquePaths(edge1[0], edge1[1])))
print('Expecting 1: {}'.format(sol.uniquePaths(edge2[0], edge2[1])))
