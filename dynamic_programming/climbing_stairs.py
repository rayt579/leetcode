'''
https://leetcode.com/problems/climbing-stairs/description/
'''

class Solution:
    num_ways_to_climb = {}

    def climbStairs_using_memoization(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            raise Exception('Cannot take negative steps')
        if n <= 1:
            return 1
        if n in self.num_ways_to_climb:
            return self.num_ways_to_climb[n]

        num_ways =  self.climbStairs(n - 2) + self.climbStairs(n - 1)
        self.num_ways_to_climb[n] = num_ways
        return num_ways

    def climbStairs(self, n):
        num_combinations = [0] * (n  + 1)
        num_combinations[0], num_combinations[1] = 1, 1
        for i in range(2, n + 1):
            num_combinations[i] = num_combinations[i - 1] + num_combinations[i - 2]
        return num_combinations[n]



sol = Solution()
print(sol.climbStairs(3))
