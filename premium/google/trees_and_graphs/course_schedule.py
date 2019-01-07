from collections import defaultdict 
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        return self.canFinishBFS(numCourses, prerequisites)

    def canFinishDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        neighbors = self.create_graph(numCourses, prerequisites)
        visited = set()
        for i in range(numCourses):
            if i not in visited:
                visiting = set()
                if self.has_cycle(i, visiting, visited, neighbors):
                    return False
        return True

    def create_graph(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        return graph

    def has_cycle(self, i, visiting, visited, neighbors):
        if i in visiting:
            return True
        visiting.add(i)
        for neighbor in neighbors[i]:
            if neighbor not in visited and self.has_cycle(neighbor, visiting, visited, neighbors):
                return True
        visiting.remove(i)
        visited.add(i)
        return False

    def canFinishBFS(self, numCourses, prerequisites):
        indegrees = [0] * numCourses
        neighbors = self.create_graph(numCourses, prerequisites)
        for u, v in prerequisites:
            indegrees[v] += 1

        ordering = []
        sources = deque([i for i in range(len(indegrees)) if indegrees[i] == 0])

        while len(sources) > 0:
            node = sources.popleft()
            ordering.append(node)
            for neighbor in neighbors[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    sources.append(neighbor)
        
        print(ordering)
        for i in indegrees:
            if i != 0:
                return False
        return True


sol = Solution()
res = sol.canFinish(5, [[0,2],[1,2],[1,4],[2,3],[4,3]])
print('Expecting True: {}'.format(res))

res2 = sol.canFinish(5, [[0,2],[1,2],[2,3],[3,4],[4,1]])
print('Expecting False: {}'.format(res2))
