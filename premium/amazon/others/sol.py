class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = []
        if m <= 0 or n <= 0:
            return res
        count = 0
        roots = [-1] * m * n

        for i, j in positions:
            root = n * i + j
            roots[root] = root
            count += 1

            for x, y in dirs:
                next_i, next_j = x + i, y + j
                nb = n * next_i + next_j
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or roots[nb] == -1:
                    continue
                root_nb = self.find_islands(roots, nb)
                if root != root_nb:
                    roots[root] = root_nb
                    root = root_nb
                    count -= 1
            res.append(count)
        return res

    def find_islands(self, roots, nb):
        while roots[nb] != nb:
            roots[nb] = roots[roots[nb]]
            nb = roots[nb]
        return nb

sol = Solution()
print('Expect [1,2,3,4,3,2,1]: {}'.format(sol.numIslands2(3,3,[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])))

