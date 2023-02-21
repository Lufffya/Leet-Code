# https://leetcode.cn/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] > j:
                    continue
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 5
    print(Solution().coinChange(coins, amount))