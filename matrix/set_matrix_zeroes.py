'''
https://leetcode.com/problems/set-matrix-zeroes/description/
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        visited_rows = set()
        visited_cols = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    visited_cols.add(j)
                    visited_rows.add(i)

        for row in visited_rows:
            for y in range(cols):
                matrix[row][y] = 0

        for col in visited_cols:
            for x in range(rows):
                matrix[x][col] = 0

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(matrix)
sol = Solution()
sol.setZeroes(matrix)
print(matrix)
