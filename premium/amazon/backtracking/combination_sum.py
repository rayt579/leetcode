'''
https://leetcode.com/explore/interview/card/amazon/84/backtracking/491/
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combination_sum_recursive(candidates, target)

    def combination_sum_recursive(self, candidates, target):
        res= []
        def helper(i, total, path):
            if total > target:
                return
            elif total == target:
                res.append(list(path))
            else:
                for j in range(i, len(candidates)):
                    path.append(candidates[j])
                    helper(j, total + candidates[j], path)
                    path.pop()
        helper(0, 0, [])
        return res

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))
