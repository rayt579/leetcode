'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
import collections
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        max_profit, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

    ProfitWithMinMax = collections.namedtuple('ProfitWithMinMax', ['profit','min','max',])

    def maxProfit_recursive(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.max_profit_recursive(prices).profit

    def max_profit_recursive(self, prices):
        if len(prices) == 1:
            return self.ProfitWithMinMax(0, prices[0], prices[0])

        mid = len(prices) // 2
        left = self.max_profit_recursive(prices[:mid])
        right = self.max_profit_recursive(prices[mid:])
        return self.ProfitWithMinMax(max(left.profit, right.profit, right.max - left.min), min(left.min, right.min), max(left.max, right.max))


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

