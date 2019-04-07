from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.cycle_detected = None

    def alienOrder(self, words):
        return self.alien_order_dfs(words)

    def alien_order_dfs(self, words):
        if not words or len(words) == 0:
            return ''

        # create adj list graph
        neighbors = {} 
        for word in words:
            for c in word:
                neighbors[c] = set()
        

        n = len(words)
        for i in range(n - 1):
            curr_word, next_word = words[i], words[i + 1]
            length = min(len(curr_word), len(next_word))
            for j in range(length):
                c1, c2 = curr_word[j], next_word[j]
                if c1 != c2:
                    neighbors[c1].add(c2)
                    break
        
        # perform a topological sort
        visited, path = set(), set()
        self.cycle_detected = False
        results = []
        for c in neighbors:
            if c not in visited:
                self.dfs(neighbors, visited, path, c, results)
        
        return ''.join(reversed(results)) if not self.cycle_detected else ''

        
    def dfs(self, graph, visited, path, curr, results):
        if not curr:
            return
        if curr in path:
            self.cycle_detected = True
            return 

        path.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                self.dfs(graph, visited, path, neighbor, results)
        
        path.remove(curr)
        visited.add(curr)
        results.append(curr)

    def alien_order_bfs(self, words):
        neighbors, indegrees = defaultdict(set), {}
        for word in words:
            for c in word:
                indegrees[c] = 0
        
        result = ''
        if not words or len(words) == 0:
            return result

        # build the adj list with neighbors
        for i in range(len(words) - 1):
            curr_word, next_word = words[i], words[i + 1]
            length = min(len(curr_word), len(next_word))
            for j in range(length):
                c1, c2 = curr_word[j], next_word[j]
                if c1 != c2:
                    curr_neighbors = neighbors[c1]
                    if c2 not in curr_neighbors:
                        curr_neighbors.add(c2)
                        indegrees[c2] += 1
                    break

        # perform topological sort
        queue = deque()
        for c in indegrees:
            if indegrees[c] == 0:
                queue.append(c)
        
        while queue:
            curr = queue.popleft()
            result += curr
            for neighbor in neighbors[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        #invalidate results if a cycle is detected
        for c in indegrees:
            if indegrees[c] != 0:
                return ''

        return result

sol = Solution()
a = sol.alienOrder(['wrt','wrf', 'er', 'ett', 'rtff'])
b = sol.alienOrder(['z', 'x', 'z'])
print('Expecting wertf: {}'.format(a))
print('Expecting empty: {}'.format(b))
