'''
https://leetcode.com/problems/house-robber-ii/description/
'''

class Solution:
    def rob_helper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sum_with_prev = 0
        sum_without_prev = 0
        for i in range(len(nums)):
            take = sum_without_prev + nums[i]
            skip = max(sum_without_prev, sum_with_prev)
            sum_with_prev = take
            sum_without_prev = skip
        return max(sum_with_prev, sum_without_prev)

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

sol = Solution()
print('Expecting 3: {}'.format(sol.rob([2,3,2])))
print('Expecting 4: {}'.format(sol.rob([1,2,3,1])))
