import bisect
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.smallest_distance_pair_using_bsearch(nums, k)

    def smallest_distance_pair_using_bsearch(self, nums, k):
        def count(nums, num):
            match_count = 0
            for i in range(len(nums)):
                j = bisect.bisect_right(nums, nums[i] + num, lo=i)
                match_count += j - i - 1
            return match_count

        nums.sort()
        n, lo, hi = len(nums), 0, nums[len(nums) - 1] - nums[0]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            pair_distance_lte = count(nums, mid)
            if pair_distance_lte < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

sol = Solution()
res = sol.smallestDistancePair([1,3,1],1)
print('Expecting 0: {}'.format(res))
