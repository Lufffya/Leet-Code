# https://leetcode.cn/problems/combination-sum-iv/

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for j in range(target + 1):
            for i in range(len(nums)):
                if nums[i] > j:
                    continue
                dp[j] += dp[j - nums[i]]
        
        return dp[-1]


if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    print(Solution().combinationSum4(nums, target))