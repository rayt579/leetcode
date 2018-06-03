'''
https://leetcode.com/problems/rotate-image/description/

Rotate a n x n matrix 90 degrees clockwise
'''

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in range(n // 2):
            for y in range(x, n - x - 1):
                temp1 = matrix[y][n - 1 - x]
                matrix[y][n - 1 - x] = matrix[x][y]

                temp2 = matrix[n - x - 1][n - y - 1]
                matrix[n - x - 1][n - y - 1] = temp1

                temp3 = matrix[n - y - 1][x]
                matrix[n - y - 1][x] = temp2

                matrix[x][y] = temp3

sol = Solution()
odd_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(odd_matrix)
print('Rotating odd 90 degrees clockwise')
sol.rotate(odd_matrix)
print(odd_matrix)

even_matrix = [[1,2],[3,4]]
print(even_matrix)
print('Rotating even 90 degrees clockwise')
sol.rotate(even_matrix)
print(even_matrix)
