class Solution(object):
	def subsets(self, nums):
	    path = [None] * len(nums)
	    subsets = []
	    self.get_all_subsets_recursive(nums, path, 0, subsets)
	    return subsets

	def get_all_subsets_recursive(self, nums, path, i, subsets):
	    if i == len(nums):
	        subset = [item for item in path if item is not None]
	        subsets.append(subset)
	    else:
	        path[i] = nums[i]
	        self.get_all_subsets_recursive(nums, path, i + 1, subsets)

	        path[i] = None
	        self.get_all_subsets_recursive(nums, path, i + 1, subsets)

sol = Solution()
print(sol.subsets([1, 2, 2]))


