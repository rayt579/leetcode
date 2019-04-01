from collections import deque

def topological_ordering_kahns(n, edges):
    graph = {i : [] for i in range(n)}
    indegrees = [0] * n
    for v, u in edges:
        graph[u].append(v)
        indegrees[v] += 1
    
    top_ordering = []
    queue = deque([i for i in range(n) if indegrees[i] == 0])
    while queue:
        curr = queue.popleft()
        top_ordering.append(curr)
        for neighbor in graph[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    for i in indegrees:
        if i != 0:
            return []
    return top_ordering

def topological_sort_dfs(n, edges):
    graph = {i : [] for i in range(n)}
    for v, u in edges:
        graph[u].append(v)
    
    ordering = []
    def dfs(curr, visited, path):
        if curr in visited:
            return 
        if curr in path:
            print('Not a DAG. Cycle detected')
            return
        path.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                dfs(neighbor, visited, path)
        path.remove(curr)
        visited.add(curr)
        ordering.append(curr)
    
    visited, path = set(), set()
    for i in range(n):
        if i not in visited:
            dfs(i, visited, path)
    return ordering[::-1] if len(ordering) == n else []


res1 = topological_ordering_kahns(8, [[3,0],[3,1],[4,1],[4,2],[7,2],[5,3],[6,3]])
res2 = topological_ordering_kahns(8, [[3,0],[3,1],[4,1],[4,2],[7,2],[5,3],[6,3],[2,7]])
dfsres1 = topological_sort_dfs(8, [[3,0],[3,1],[4,1],[4,2],[7,2],[5,3],[6,3]])
dfsres2 = topological_sort_dfs(8, [[3,0],[3,1],[4,1],[4,2],[7,2],[5,3],[6,3],[2,7]])

print('expecting {}: {}'.format(range(8), res1))
print('expecting []: {}'.format(res2))
print('expecting {}: {}'.format(range(8), dfsres1))
print('expecting []: {}'.format(dfsres2))
