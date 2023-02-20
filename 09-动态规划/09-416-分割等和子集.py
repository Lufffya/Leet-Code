# https://leetcode.cn/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        bag_size = target = sum(nums) // 2
        dp = [0] * (target + 1)

        for i in range(len(nums)):
            for j in range(bag_size, 0, -1):
                if nums[i] > j:
                    continue
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[-1] == target


if __name__ == "__main__":
    nums = [1,2,5]
    print(Solution().canPartition(nums))