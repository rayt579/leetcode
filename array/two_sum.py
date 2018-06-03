'''
https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_seen_so_far_indices = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_seen_so_far_indices:
                return [nums_seen_so_far_indices[complement], i]
            nums_seen_so_far_indices[nums[i]] = i
        return None

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
indices = sol.twoSum(nums, target)
print('Expecting [0, 1]: {}'.format(indices))
