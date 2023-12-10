#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                best_profit=max(best_profit, prices[right] - prices[left])
            else:
                left = right
            
            right += 1

        return best_profit