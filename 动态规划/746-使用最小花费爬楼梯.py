# https://leetcode.cn/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(cost[i] + dp[i - 2], cost[i] + dp[i - 1])

        return min(dp[-2], dp[-1])


if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    r = Solution().minCostClimbingStairs(cost)
    print(r)
