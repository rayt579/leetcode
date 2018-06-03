'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''

import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        element_counts = collections.Counter(nums)
        count_maxheap = []
        for el, count in element_counts.items():
            heapq.heappush(count_maxheap, (-count, el))

        top_k_frequent_els = [heapq.heappop(count_maxheap)[1] for _ in range(k)]
        return top_k_frequent_els


a = [1,2,3,2]
b = [1,1,1,2,2,3]

sol = Solution()
print(sol.topKFrequent(a, 1))
print(sol.topKFrequent(a, 2))
print(sol.topKFrequent(a, 3))
print(sol.topKFrequent(b, 2))
