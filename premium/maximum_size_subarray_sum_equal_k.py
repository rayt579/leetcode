'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/524/
'''

class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prev_sums = {}
        curr_sum, max_len = 0, 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == k:
                max_len = max(max_len, i + 1)
            elif curr_sum - k in prev_sums:
                max_len = max(max_len, i - prev_sums[curr_sum - k])

            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = i
        return max_len

a = [1,-1,5,-2,3]
b = [-2,-1,2,1]
c = [-1, 1]
sol = Solution()

print('Expecting 4: {}'.format(sol.maxSubArrayLen(a, 3)))
print('Expecting 2: {}'.format(sol.maxSubArrayLen(b, 1)))
print('Expecting 0: {}'.format(sol.maxSubArrayLen(a, 10)))
print('Expecting 1: {}'.format(sol.maxSubArrayLen(c, 1)))
