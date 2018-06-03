'''
https://leetcode.com/problems/longest-increasing-subsequence/description/
'''

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = [nums[0]]
        for i in range(1, len(nums)):
            if tails[-1] < nums[i]:
                tails.append(nums[i])
            else:
                length_index = self.find_slot(tails, nums[i])
                tails[length_index] = nums[i]
        return len(tails)

    def find_slot(self, A, val):
        if not A or A[-1] < val:
            raise Exception('No slot found')

        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = (hi - lo)//2 + lo
            if A[mid] == val:
                if mid - 1 >= 0 and A[mid - 1] < A[mid]:
                    return mid
                hi = mid - 1
            elif A[mid] < val:
                if mid + 1 < len(A) and A[mid + 1] > val:
                    return mid + 1
                lo  = mid + 1
            else:
                hi = mid - 1
        return 0

    def length_of_longest_increasing_subsequence_bottomup(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length_lis = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length_lis[i] = max(length_lis[i], length_lis[j] + 1)
        return max(length_lis)

sol = Solution()


#find_slot_unit_tests
print('Unit tests for binary search implementation......')
print('Expect index 0: {}'.format(sol.find_slot([4,5,6,7], 3)))
print('Expect index 4: {}'.format(sol.find_slot([4,5,6,7,12], 8)))
print('Expect index 2: {}'.format(sol.find_slot([4,6,10,12], 8)))
print('Unit tests for LIS............')
print('Expecting length of 6: {}'.format(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])))
print('Expecting length of 4: {}'.format(sol.lengthOfLIS([10,9,2,5,3,7,101,18])))
print('Expecting length of 6: {}'.format(sol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])))
