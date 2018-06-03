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
        score = [float('-inf')] * len(nums)
        score[0] = nums[0]
        max_score = score[0]

        for i in range(1, len(nums)):
            score[i] = max(nums[i] + score[i - 1], nums[i])
            max_score = max(max_score, score[i])

        return max_score

sol = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1,2]
print('Expect 6: {}'.format(sol.maxSubArray(a)))
print('Expect 3: {}'.format(sol.maxSubArray(b)))

