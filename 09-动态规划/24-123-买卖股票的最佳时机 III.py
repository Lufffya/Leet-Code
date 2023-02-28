# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0,0,0,0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        
        return max(dp[-1])


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))