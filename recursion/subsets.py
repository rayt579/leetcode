'''
https://leetcode.com/problems/subsets/description/
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = set()
        self.subsets_recursive(nums, subsets)
        list_of_subsets = [list(subset) for subset in subsets]
        list_of_subsets.append([])
        return list_of_subsets

    def subsets_recursive(self, nums, all_possible_subsets):
        subset = tuple(nums)

        if subset in all_possible_subsets:
            return

        if len(nums) > 1:
            for i in range(len(nums)):
                self.subsets_recursive(nums[:i] + nums[i+1:], all_possible_subsets)

        all_possible_subsets.add(subset)

sol = Solution()
print(sol.subsets([1,2,3]))
