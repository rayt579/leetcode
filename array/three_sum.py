'''
https://leetcode.com/problems/3sum/description/
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        if not nums:
            return triplets

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            expected_sum = -nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] == expected_sum:
                    triplets.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] > expected_sum:
                    hi -= 1
                else:
                    lo += 1
        return triplets


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print('Expecting [-1,0,1], [-1,-1,2]: {}'.format(sol.threeSum(nums)))
print('Expecting [0, 0, 0]: {}'.format(sol.threeSum([0,0,0,1000,0, 2004])))
print('Expecting []: {}'.format(sol.threeSum([0,1000,0, 2004])))
