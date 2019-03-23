class Solution:
    def prisonAfterNDays(self, cells, N):
        seen = {''.join(str(c) for c in cells) : N}
        while N:
            seen.setdefault(''.join(str(c) for c in cells), N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            k = ''.join(str(c) for c in cells)
            if k in seen:
                N %= seen[k] - N
        return cells

    def prison_after_n_days_optimized(self, cells, N):

sol = Solution()
print(sol.prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
print(sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
