'''
https://leetcode.com/explore/interview/card/amazon/82/others/898/
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

sol = Solution()
print('Expect 2: {}'.format(sol.singleNumber([1,2,1,3,4,5,5,4,3])))
