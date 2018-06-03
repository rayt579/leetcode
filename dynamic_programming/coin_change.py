'''
https://leetcode.com/problems/coin-change/description/
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        amounts = [0] * (amount + 1)
        for current_amount in range(1, len(amounts)):
            min_coins_at_current = float('inf')
            for coin in coins:
                if current_amount >= coin:
                    min_coins_at_current = min(min_coins_at_current, amounts[current_amount - coin] + 1)

            amounts[current_amount] = min_coins_at_current

        return amounts[amount] if amounts[amount] != float('inf') else -1


sol = Solution()
print(sol.coinChange([1,2], 4))
print(sol.coinChange([1, 3, 5], 6))
print(sol.coinChange([3, 5], 2))

