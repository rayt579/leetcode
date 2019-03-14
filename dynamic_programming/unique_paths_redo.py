class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            path[i][0] = 1
        for j in range(m):
            path[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[n - 1][m - 1]
sol = Solution()
print(sol.uniquePaths(3, 2))

        
