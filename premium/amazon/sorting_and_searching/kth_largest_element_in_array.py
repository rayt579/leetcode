'''
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/482/
'''
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find_kth_largest_heap(nums, k)

    def find_kth_largest_inplacesort(self, nums, k):
        if not nums:
            return None
        nums.sort()
        return nums[-k]

    def find_kth_largest_heap(self, nums, k):
        if not nums:
            return None
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

sol = Solution()
print('Expecting 5: {}'.format(sol.findKthLargest([3,2,1,5,6,4], 2)))
print('Expecting 4: {}'.format(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)))
