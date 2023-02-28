# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] + ((2 * k) * [0]) for _ in range(len(prices))]
        
        for _k in range(1, len(dp[0]), 2):
            dp[0][_k] = -prices[0]

        for i in range(1, len(prices)):
            for _k in range(len(dp[0])):
                if _k == 0:
                    dp[i][_k] = dp[i - 1][_k]
                elif _k % 2 == 0:
                    dp[i][_k] = max(dp[i - 1][_k], dp[i - 1][_k - 1] + prices[i])
                else:
                    dp[i][_k] = max(dp[i - 1][_k], dp[i - 1][_k - 1] - prices[i])
        
        return max(dp[-1])


if __name__ == '__main__':
    k = 2
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(k, prices))