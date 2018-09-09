'''
https://leetcode.com/problems/maximum-subarray/description/
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        curr_sum, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            res = max(res, curr_sum)
        return res

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

