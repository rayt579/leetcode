import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    def find_kth_largest_quicksort(self, nums, k):
        if not nums:
            return None

        target_partition = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            j = self.partition(nums, lo, hi)
            if j == target_partition:
                return nums[j]
            elif j > target_partition:
                hi = j - 1
            else:
                lo = j + 1
        return -1
    
    def partition(self, nums, lo, hi):
        i, j = lo, hi
        while True:
            while i < hi and nums[i] <= nums[lo]:
                i += 1
            while j > lo and nums[j] > nums[lo]:
                j -= 1
            if i >= j: 
                break

            nums[i], nums[j] = nums[j], nums[i]
        
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

sol = Solution()
print('Expecting 5: {}'.format(sol.findKthLargest([3,2,1,5,6,4], 2)))
print('Expecting 4: {}'.format(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)))
print('Expecting 1: {}'.format(sol.find_kth_largest_quicksort([1], 1)))
