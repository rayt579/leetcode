class Solution:
    def cutOffTree(self, forest):
        if not forest or len(forest) == 0:
            return 0

        m, n = len(forest), len(forest[0])
        min_heap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(pq, (forest[i][j], i, j))

        start = [0] * 2
        min_steps = 0

        while len(pq) > 0:
            tree = heapq.heappop(pq)
            step = self.min_step(forest, start, tree, m, n)
            if step < 0:
                return -1
            min_steps += step
            start[0] = tree[0]
            start[1] = tree[1]

        return min_steps 

    def min_step(forest, start, tree, m, n):
        step = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            size = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr[0] == tree[0] and curr[1] == tree[1]:
                    return step
                for x, y in [(curr[0] - 1, curr[1]), (curr[0] + 1, curr[1]), (curr[0], curr[1] - 1), (curr[0], curr[1] + 1):
                        if 0 <= x < m and 0 <= y < n and not visited[x][y] and forest[x][y] != 0:
                            queue.append([x, y])
                            visited[x][y] = True
            step += 1
        return -1
      

sol = Solution()
a = [[1,2,3],[0,0,4],[7,6,5]]
print('Expecting 6: {}'.format(sol.cutOffTree(a)))
