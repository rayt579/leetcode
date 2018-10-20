'''
https://leetcode.com/explore/featured/card/google/59/array-and-strings/338/'
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        M, N = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0 
        while i < M - i and j < N - j:
            for x in range(j, N - j):
                res.append(matrix[i][x])
            for x in range(i + 1, M - i):
                res.append(matrix[x][N - j - 1])
            
            if M - i - 1 > i:
                for x in range(N - j - 2, j - 1, -1):
                    res.append(matrix[M - i - 1][x])
            if N - j - 1 > j:
                for x in range(M - i - 2, i, -1):
                    res.append(matrix[x][j])

            i += 1
            j += 1

        return res

sol = Solution()
matrix1 = [[1,2],[3,4]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix4 = [[1,2,3]]

print('Spiral order: {}'.format(sol.spiralOrder(matrix1)))
print('Spiral order: {}'.format(sol.spiralOrder(matrix2)))
print('Spiral order: {}'.format(sol.spiralOrder(matrix3)))
print('Spiral order: {}'.format(sol.spiralOrder(matrix4)))
