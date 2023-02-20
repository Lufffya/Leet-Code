# https://leetcode.cn/problems/last-stone-weight-ii/

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        bag_size = sum(stones) // 2
        dp = [0] * (bag_size + 1)

        for i in range(len(stones)):
            for j in range(bag_size, 0, -1):
                if stones[i] > j:
                    continue
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sum(stones) - (dp[-1] * 2)


if __name__ == "__main__":
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeightII(stones))