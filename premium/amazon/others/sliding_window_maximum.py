from collections import deque
class Solution:
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		return self.max_sliding_window_queue(nums, k)

	def max_sliding_window_bf(self, nums, k):
		if not nums:
			return []
		return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

	def max_sliding_window_queue(self, nums, k):
		if not nums: return []
		results = []
		queue = deque()
		for i in range(len(nums)):
			if len(queue) > 0 and queue[0] <= i - k:
				queue.popleft()
			while len(queue) > 0 and nums[queue[-1]] < nums[i]:
				queue.pop()
			queue.append(i)
			if i >= k - 1:
				results.append(nums[queue[0]])
		return results

sol = Solution()
print('Expecting [3,3,5,5,6,7]: {}'.format(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)))
