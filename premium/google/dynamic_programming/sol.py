class Solution:
    def maxVacationDays(self, flights, days):
        N, K = len(flights), len(days[0])
        dp = [float('-inf')] * N
        dp[0] = 0
        for i in range(K):
            temp = [float('-inf')] * N
            for j in range(N):
                for k in range(N):
                    if j == k or flights[k][j] == 1:
                        temp[j] = max(temp[j], dp[k] + days[j][i])
            dp = temp
        return max(dp)
sol = Solution()
flights = [[0, 1, 1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]
res = sol.maxVacationDays(flights, days)
print('Expecting 12: {}'.format(res))
