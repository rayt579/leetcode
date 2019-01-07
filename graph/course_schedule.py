'''
https://leetcode.com/problems/course-schedule/description/
'''
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        to_visit = collections.deque([])
        for a, b in prerequisites:
            indegree[b] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                to_visit.append(i)
        while to_visit:
            node = to_visit.popleft()
            for a, b in prerequisites:
                if a == node:
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        to_visit.append(b)
        for degree in indegree:
            if degree != 0:
                return False
        return True

    def canFinishRecursive(self, numCourses, prerequisites):
        graph = {i : [] for i in range(numCourses)}
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        to_visit = set(graph.keys())
        is_visiting = set()
        visited = set()

        while to_visit:
            node = next(iter(to_visit))
            if self.dfs_has_cycle(graph, node, to_visit, is_visiting, visited):
                return False
        return True

    def dfs_has_cycle(self, graph, node, to_visit, visiting, is_visited):
        if node in visiting:
            return True
        if node in to_visit:
            to_visit.remove(node)
        visiting.add(node)
        for neighbor in graph[node]:
            if self.dfs_has_cycle(graph, neighbor, to_visit, visiting, is_visited):
                return True
        visiting.remove(node)
        is_visited.add(node)
        return False

sol = Solution()
print('Expected True: {}'.format(sol.canFinish(2, [[1,0]])))
print('Expected False: {}'.format(sol.canFinish(2, [[1, 0], [0,1]])))
print('Expected True: {}'.format(sol.canFinish(3, [[0,1],[0,2],[1,2]])))
