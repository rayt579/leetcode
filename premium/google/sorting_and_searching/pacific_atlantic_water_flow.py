class Solution:
    def pacificAtlantic(self, matrix: 'List[List[int]]') -> 'List[List[int]]':
        def dfs(i, j, visited):
            visited[i][j] = True
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not 0 <= x < len(matrix) or not 0 <= y < len(matrix[0]) or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                visited[x][y] = True
                dfs(x, y, visited)

        if not matrix or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        reaches_pacific = [[False for _ in range(n)] for _ in range(m)]
        reaches_atlantic = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dfs(i, 0, reaches_pacific)
            dfs(i, n - 1, reaches_atlantic)
        for j in range(n):
            dfs(0, j, reaches_pacific)
            dfs(m - 1, j, reaches_atlantic)
        
        reaches_both_oceans = []
        for i in range(m):
            for j in range(n):
                if reaches_atlantic[i][j] and reaches_pacific[i][j]:
                    reaches_both_oceans.append([i, j])
        return reaches_both_oceans

sol = Solution()
#matrix = [[1,2,2,3,5],[3, 2, 3, 4, 4],[2, 4, 5, 3, 1],[6, 7, 1, 4, 5],[5, 1, 1, 2, 4]]
sol_matrix = [[10,7,7,9,17,0,8,8,18,9,4,6,13,18,11,3,18,1,10,5,16,12,9],[16,14,9,8,19,14,9,7,15,9,18,12,2,11,10,18,16,3,0,16,14,10,14],[6,13,5,2,12,7,6,2,2,10,2,7,0,12,13,14,8,18,17,2,9,14,12],[2,19,8,10,14,9,6,8,1,2,7,4,10,0,2,1,13,19,0,14,6,3,3],[6,15,14,19,19,11,17,16,18,15,13,2,11,18,2,9,11,18,8,16,18,9,10],[8,6,15,8,3,14,0,0,4,7,18,13,11,7,5,9,0,19,15,6,16,15,13],[16,8,2,11,9,18,8,8,2,4,13,12,1,16,18,11,12,18,3,9,2,0,3],[17,13,19,1,12,5,16,18,9,19,6,15,14,6,4,9,6,19,12,10,10,19,1],[19,11,11,6,5,5,7,15,6,18,13,9,6,15,18,4,14,4,10,8,16,8,17],[18,1,7,9,0,16,3,8,12,1,14,8,15,6,6,6,1,9,0,4,1,7,0],[5,2,5,13,7,10,10,13,16,16,5,7,14,1,1,8,6,3,18,18,12,6,3],[8,18,16,6,4,2,16,8,6,10,4,15,9,15,3,14,8,2,10,8,15,4,14],[12,1,16,0,9,10,15,10,2,6,3,2,1,13,5,17,5,10,2,8,11,7,17],[15,6,7,3,4,15,2,11,16,8,6,2,18,11,15,16,0,16,10,1,1,9,11],[15,17,10,17,19,12,1,11,19,3,15,4,16,18,1,0,5,19,18,14,0,0,14],[7,4,19,13,2,13,11,2,18,12,19,19,12,11,3,10,5,5,15,13,8,3,0]]

#print(sol.pacificAtlantic(matrix))
print(sol.pacificAtlantic(sol_matrix))
