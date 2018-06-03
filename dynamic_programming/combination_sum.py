'''
https://leetcode.com/problems/combination-sum-iv/description/
'''


class Solution:
    def combination_sum4_topdown_with_memoization(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        combination_sum_at = dict()

        def helper(target):
            if target in combination_sum_at:
                return combination_sum_at[target]
            if target == 0:
                return 1
            else:
                count = 0
                for num in nums:
                    if target >= num:
                        count += helper(target - num)

                combination_sum_at[target] = count
                return count

        return helper(target)

    def combinationSum4(self, nums, target):
        if target == 0:
            return 0
        combination_sum = [0] * (target + 1)
        combination_sum[0] = 1
        for current_target in range(1, target + 1):
            for num in nums:
                if current_target >= num:
                    combination_sum[current_target] += combination_sum[current_target - num]

        return combination_sum[current_target]

sol = Solution()
print(sol.combinationSum4([2,1,3], 4))
