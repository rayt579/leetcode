'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/496/
'''

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_duplicate_modified_bsearch(nums)

    # O(n log n) time, O(1) space. This solution is stable and takes advantage of bsearch.
    def find_duplicate_modified_bsearch(self, nums):
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = lo + (hi-lo)//2
            freq_left = 0
            slots_available = mid - lo + 1
            for i in range(len(nums)):
                if lo <= nums[i] <= mid:
                    freq_left += 1
            if freq_left > slots_available:
                hi = mid
            else:
                lo = mid + 1

        return lo


sol = Solution()
a = [1,3,4,2,2]
b = [3,1,3,4,2]
c = [2,2,2,2]

print('Expect 2: {}'.format(sol.findDuplicate(a)))
print('Expect 3: {}'.format(sol.findDuplicate(b)))
print('Expect 2: {}'.format(sol.findDuplicate(c)))
