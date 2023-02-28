# https://leetcode.cn/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        _max = 0

        for _nums in [nums[1:], nums[:-1]]:

            if len(_nums) == 1:
                _max = max(_max, _nums[0])
                continue

            dp = [0] * len(_nums)
            dp[0] = _nums[0]
            dp[1] = max(_nums[0], _nums[1])

            for i in range(2, len(_nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + _nums[i])

            _max = max(_max, dp[-1])

        return _max


if __name__ == '__main__':
    nums = [0,0]
    print(Solution().rob(nums))