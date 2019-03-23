class Solution:
    def cutOffTree(self, forest):
        return -1

tc1 = [[1,2,3],[0,0,4],[7,6,5]]
tc2 = [[1,2,3],[0,0,0],[7,6,5]]
tc3 = [[2,3,4],[0,0,5],[8,7,6]]

sol = Solution()
print('Expecting 6: {}'.format(sol.cutOffTree(tc1)))
print('Expecting -1: {}'.format(sol.cutOffTree(tc2)))
print('Expecting 6: {}'.format(sol.cutOffTree(tc3)))
