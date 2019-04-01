from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        return self.can_finish_dfs(numCourses, prerequisites)
    
    def can_finish_dfs(self, n, prerequisites):
        graph = { i : [] for i in range(n) }
        for v, u in prerequisites:
            graph[u].append(v)
        visited, path = set(), set()
        for i in range(n):
            if i not in visited and self.has_cycle(i, visited, path, graph):
                return False
        return True

    def has_cycle(self, curr, visited, path, graph):
        if curr in visited:
            return False
        if curr in path:
            return True
        path.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited and self.has_cycle(neighbor, visited, path, graph):
                return True
        path.remove(curr)
        visited.add(curr)
        return False

    def can_finish_bfs(self, n, prerequisites):
        graph = {i : [] for i in range(n)}
        indegrees = [0] * n
        for v, u in prerequisites:
            graph[u].append(v)
            indegrees[v] += 1
        queue = deque([i for i in range(n) if indegrees[i] == 0])
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        for i in indegrees:
            if i != 0: 
                return False
        return True

sol = Solution()
res = sol.canFinish(5, [[2, 0], [2, 1], [3, 2], [4, 2]])
print('Expecting True: {}'.format(res))

negative = sol.canFinish(3, [[2, 0], [0, 2]])
print('Expecting False: {}'.format(negative))
