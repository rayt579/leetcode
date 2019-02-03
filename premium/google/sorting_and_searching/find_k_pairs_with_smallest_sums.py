import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        min_heap, k_pairs_with_smallest_sum = [], []
        initial_heap_count = k if k < len(nums1) else len(nums1)
        for i in range(initial_heap_count):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], [nums1[i], nums2[0]], 0))

        while len(min_heap) > 0 and len(k_pairs_with_smallest_sum) < k:
            _, pair, nums2_index = heapq.heappop(min_heap)
            k_pairs_with_smallest_sum.append(pair)
            if nums2_index + 1 < len(nums2):
                heapq.heappush(min_heap, (pair[0] + nums2[nums2_index + 1], [pair[0], nums2[nums2_index + 1]], nums2_index + 1))
        
        return k_pairs_with_smallest_sum

sol = Solution()
res = sol.kSmallestPairs([1, 7, 11, 16], [2, 9, 10, 15], 4)
print('Expecting [1, 2], [7, 2], [1, 9], [1, 10]: {}'.format(res))
