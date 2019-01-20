class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip =  [[0 for _ in range(10)] for _ in range(10)]
        visited = [False] * 10
        skip[1][3], skip[3][1] = 2, 2
        skip[1][7], skip[7][1] = 4, 4
        skip[3][9], skip[9][3] = 6, 6
        skip[7][9], skip[9][7] = 8, 8
        skip[2][8], skip[8][2], skip[4][6], skip[6][4], skip[1][9], skip[9][1], skip[3][7], skip[7][3] = 5, 5, 5, 5, 5, 5, 5, 5
        print(skip)
        total = 0
        total += self.dfs(1, 1, visited, 0, m, n, skip) * 4
        total += self.dfs(2, 1, visited, 0, m, n, skip) * 4
        total += self.dfs(5, 1, visited, 0, m, n, skip)
        return total
    
    def dfs(self, curr_num, curr_length, visited, total, m, n, skip):
        if curr_length >= m:
            total += 1
        if curr_length == n:
            return total

        visited[curr_num] = True
        for next_num in range(1, 10):
            if not visited[next_num] and (skip[curr_num][next_num] == 0 or visited[skip[curr_num][next_num]]):
                total += self.dfs(next_num, curr_length + 1, visited, 0, m, n, skip)

        visited[curr_num] = False
        return total

sol = Solution()
print(sol.numberOfPatterns(1,1))
#print(sol.numberOfPatterns(1,2))
