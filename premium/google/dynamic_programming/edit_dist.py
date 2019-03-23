class Solution:
    def min_distance_topdown_memo(self, word1: str, word2: str) -> int:
        results = {}
        m, n = len(word1), len(word2)
        def min_edit_distance(i, j, dist):
            if i == m and j == n:
                return dist
            elif i == m:
                return dist + n - j
            elif j == n:
                return dist + m - i

            point = (i, j, dist)
            if point in results:
                return results[point]

            min_dist = float('inf')
            if word1[i] == word2[j]:
                min_dist = min_edit_distance(i + 1, j + 1, dist)
            else:
                replace = min_edit_distance(i + 1, j + 1, dist + 1)
                insert = min_edit_distance(i, j + 1, dist + 1)
                delete = min_edit_distance(i + 1, j, dist + 1)
                min_dist = min(replace, insert, delete)
            
            results[point] = min_dist
            return min_dist

        return min_edit_distance(0, 0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        return self.min_distance_linear_optimized(word1, word2)

    def min_distance_dp(self, word1, word2):
        m, n = len(word1), len(word2)
        min_edits = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        #Base case - empty word
        for i in range(1, m + 1):
            min_edits[i][0] = i
        for j in range(1, n + 1):
            min_edits[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    min_edits[i][j] = min_edits[i - 1][j - 1]
                else:
                    min_edits[i][j] = min(min_edits[i - 1][j - 1], min_edits[i][j - 1], min_edits[i - 1][j]) + 1
        
        return min_edits[m][n]

    def min_distance_linear_space(self, word1, word2):
        m, n = len(word1), len(word2)

        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for j in range(1, n + 1):
            prev[j] = j

        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(prev[j - 1], curr[j - 1], prev[j]) + 1
            prev = [0] * (n + 1)
            curr, prev = prev, curr
        return prev[n]

    def min_distance_linear_optimized(self, word1, word2):
        m, n = len(word1), len(word2)
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            curr[j] = j
        for i in range(1, m + 1):
            prev = curr[0]
            curr[0] = i
            for j in range(1, n + 1):
                temp = curr[j]
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev
                else:
                    curr[j] = min(curr[j], prev, curr[j - 1]) + 1
                prev = temp
        return curr[n]


sol = Solution()
res = sol.minDistance('horse', 'ros')
print('Expecting result of 3: {}'.format(res))
