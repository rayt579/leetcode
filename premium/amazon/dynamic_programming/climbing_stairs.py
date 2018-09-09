'''
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/900/
'''
class Solution:
    def __init__(self):
        self.res = None

    def climbStairs(self, n):
    	return self.climb_stairs_bottom_up(n)

    def climb_stairs_topdown_memoize(self, n):
        self.results = {}
        def helper(n):
            if n in self.results:
                return self.results[n]
            if n < 0:
                res = 0
            elif n == 0:
                res = 1
            else:
                res = helper(n - 1) + helper(n - 2)

            self.results[n] = res
            return res

        if n == 0:
            return 0
        return helper(n)

    def climb_stairs_bottom_up(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a

sol = Solution()
print('Expect 2: {}'.format(sol.climbStairs(2)))
print('Expect 3: {}'.format(sol.climbStairs(3)))

