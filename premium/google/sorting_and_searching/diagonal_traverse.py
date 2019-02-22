class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        i, j, d = 0, 0, 1
        diagonal_order = []

        while i != m - 1 or j != n - 1:
            if i < 0 and j == n:
                i += 2
                j -= 1
                d *= -1
            elif i < 0:
                i += 1
                d *= -1
            elif i == m:
                i -= 1
                j += 2
                d *= -1
            elif j < 0:
                j += 1
                d *= -1
            else:
                diagonal_order.append(matrix[i][j])
                i -= d
                j += d

        diagonal_order.append(matrix[i][j])
        return diagonal_order 

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
single_row = [[1,2,3]]
single_col = [[1],[4],[7]]
square = [[1,2],[3,4]]

traversal = sol.findDiagonalOrder(matrix)
single_row_traversal = sol.findDiagonalOrder(single_row)
single_col_traversal = sol.findDiagonalOrder(single_col)
square_traversal = sol.findDiagonalOrder(square)

print('Matrix: {}'.format(traversal))
print('Single row: {}'.format(single_row_traversal))
print('Single col: {}'.format(single_col_traversal))
print('Square: {}'.format(square_traversal))
