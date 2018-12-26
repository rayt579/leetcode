from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        #return [self.dfs(num, denom, 1.0, set(), graph) for num, denom in queries]
        return [self.bfs_iterative(num, denom, graph) for num, denom in queries]
    
    def dfs(self, start, end, value, path, graph):
        if start in path or start not in graph or end not in graph:
            return -1.0
        if start == end:
            return value
        path.add(start)
        temp = 0
        for adj, weight in graph[start]:
            temp = self.dfs(adj, end, value * weight, path, graph)
            if temp != -1.0:
                break
        path.remove(start)
        return temp 

    def bfs_iterative(self, start, end, graph):
        if start not in graph or end not in graph:
            return -1.0

        visited = set()
        score = 1.0
        queue = deque([(start, 1.0)])

        while len(queue) > 0:
            curr, score = queue.popleft()
            if curr == end:
                return score
            else:
                if curr not in visited:
                    visited.add(curr)
                    for neighbor, neighbor_weight in graph[curr]:
                        if neighbor not in visited:
                            queue.append((neighbor, score * neighbor_weight))
        return -1.0

sol = Solution()
pairs = [['a','b'],['b','c']]
values = [2.0, 3.0]
queries = [['a','c'],['b','a'],['a','e'],['a','a'],['x','x']]
res = sol.calcEquation(pairs, values, queries)
print(res)

pairs2 = [['a','b'],['c','d']]
values2 = [1.0, 1.0]
queries2 = [['a','c'],['b','d'],['b','a'],['d','c']]
res2 = sol.calcEquation(pairs2, values2, queries2)
print(res2)
