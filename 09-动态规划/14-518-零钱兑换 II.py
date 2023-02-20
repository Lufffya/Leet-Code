# https://leetcode.cn/problems/coin-change-ii/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] > j:
                    continue

                dp[j] += dp[j - coins[i]]
        
        return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))