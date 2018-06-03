'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
'''

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return len(nums)

        lcs_length = 0
        explore = set(nums)
        for num in nums:
            if num - 1 not in explore:
                next_num = num + 1
                while next_num in explore:
                    next_num += 1
                lcs_length = max(lcs_length, next_num - num)

        return lcs_length

    def longest_consecutive_sequeunce_dp(self, nums):
        lcs = {}
        max_length = 0
        for num in nums:
            if num in lcs:
                continue

            left_val = lcs[num-1] if num - 1 in lcs else 0
            right_val = lcs[num+1] if num + 1 in lcs else 0

            lcs[num] = left_val + right_val + 1
            max_length = max(max_length, lcs[num])

            lcs[num - left_val] = lcs[num]
            lcs[num + right_val] = lcs[num]

        return max_length

    def longest_consecutive_sequence_sort(self, nums):
        if not nums or len(nums) == 1:
            return len(nums)

        nums.sort()
        prev, curr = 0, 1
        cs_length, lcs_length = 1, 0
        while curr < len(nums):
            if nums[curr] == nums[prev] + 1:
                cs_length += 1
            elif nums[curr] != nums[prev]:
                cs_length = 1

            lcs_length = max(lcs_length, cs_length)
            prev = curr
            curr = curr + 1

        return lcs_length

sol = Solution()
a = [100, 4, 200, 1, 3, 2]
print('Expect 4: {}'.format(sol.longestConsecutive(a)))
