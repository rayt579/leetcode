'''
https://leetcode.com/problems/spiral-matrix/description/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        curr_col, curr_row = 0, 0
        if not matrix:
            return []

        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1
        while curr_row <= last_row and curr_col <= last_col:
            for j in range(curr_col, last_col + 1):
                spiral.append(matrix[curr_row][j])
            curr_row += 1

            for i in range(curr_row, last_row + 1):
                spiral.append(matrix[i][last_col])
            last_col -= 1

            if curr_row <= last_row:
                for j in range(last_col, curr_col - 1, -1):
                    spiral.append(matrix[last_row][j])
                last_row -= 1

            if curr_col <= last_col:
                for i in range(last_row, curr_row - 1, -1):
                    spiral.append(matrix[i][curr_col])
                curr_col += 1

        return spiral

sol = Solution()

happyspiral = sol.spiralOrder([[1,2,3],[4, 5, 6],[7,8,9]])
singleel = sol.spiralOrder([[1]])
notsquarematrix = sol.spiralOrder([[1,2],[3,4],[5,6],[7,8]])
onecol = sol.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print('Expecting 123698745: {}'.format(happyspiral))
print('Expecting 1: {}'.format(singleel))
print('Expecting 12468753: {}'.format(notsquarematrix))
print('Expecting 12345678910: {}'.format(onecol))

