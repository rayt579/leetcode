'''
https://leetcode.com/problems/subsets-ii/description/
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        nums.sort()
        self.subsets_with_backtracking(nums, [], subsets, 0)
        return subsets

    def subsets_with_backtracking(self, nums, path, subsets, start):
        subsets.append(list(path))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.subsets_with_backtracking(nums, path, subsets, i + 1)
            path.pop()

sol = Solution()
print(sol.subsetsWithDupe([1, 2, 2, 2, 2]))
