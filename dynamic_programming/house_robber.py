'''
https://leetcode.com/problems/house-robber/description/
'''

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_with_prev, sum_without_prev = 0, 0

        for i in range(len(nums)):
            take_i = sum_without_prev + nums[i]
            skip_i = max(sum_without_prev, sum_with_prev)

            sum_with_prev = take_i
            sum_without_prev = skip_i

        return max(sum_without_prev, sum_with_prev)

sol = Solution()

a = [8, 4, 5, 3]
print('Expect 13: {}'.format(sol.rob(a)))

b = [0,3,2,0,4,15,6]
print('Expect 18: {}'.format(sol.rob(b)))
