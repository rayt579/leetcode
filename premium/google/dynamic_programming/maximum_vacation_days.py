class Solution:
    def __init__(self):
        self.results = None

    def maxVacationDays(self, flights, days):
        self.results = {}
        n, k = len(flights), len(days[0])

        def dfs(curr_city, curr_week):
            if curr_week == k:
                return 0

            point = (curr_city, curr_week)

            if point in self.results:
                return self.results[point]

            max_vacation_days = float('-inf')
            for i in range(n):
                if i == curr_city or flights[curr_city][i] == 1:
                    vacation_days = dfs(i, curr_week + 1) + days[i][curr_week]
                    max_vacation_days = max(max_vacation_days, vacation_days)

            self.results[point] = max_vacation_days
            return max_vacation_days

        return dfs(0, 0)

    def max_vacation_days(self, flights, days):
        NINF = float('-inf')
        n, k = len(flights), len(days[0])
        dp = [NINF] * n
        dp[0] = 0
        for curr_week in range(k):
            temp = [NINF] * n
            for curr_city in range(n):
                for next_city in range(n):
                    if curr_city == next_city or flights[curr_city][next_city] == 1:
                        temp[next_city] = max(temp[next_city], dp[k] + days[next_city][k])
            dp = temp
        return max(dp)


sol = Solution()
flights = [[0, 1, 1],[1,0,1],[1, 1, 0]]
days = [[1, 3, 1],[6, 0, 3],[3,3,3]]
res = sol.maxVacationDays(flights, days)
print('Expecting 12: {}'.format(res))
