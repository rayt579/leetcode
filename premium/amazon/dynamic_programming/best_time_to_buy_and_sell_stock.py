'''
https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/505/
'''
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, prices[i])
        return max_profit

sol = Solution()
print('Expecting 5: {}'.format(sol.maxProfit([7,1,5,3,6,4])))
print('Expecting 0: {}'.format(sol.maxProfit([7,4,3,2,1])))

