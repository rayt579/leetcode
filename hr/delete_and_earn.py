'''
https://leetcode.com/problems/delete-and-earn/description/
'''

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        scores = [0] * 10001
        for num in nums:
            scores[num] += num

        sum_for_previous, sum_without_previous = 0, 0
        for score in scores:
            take_i = sum_without_previous + score
            skip_i = max(sum_without_previous, sum_for_previous)
            sum_for_previous = take_i
            sum_without_previous = skip_i
        return max(sum_for_previous, sum_without_previous)

sol = Solution()
print('Expecting 6: {}'.format(sol.deleteAndEarn([3,4,2])))
print('Expecting 9: {}'.format(sol.deleteAndEarn([2,2,3,3,3,4])))
print('Expecting 18: {}'.format(sol.deleteAndEarn([1,1,1,2,4,5,5,5,6])))
