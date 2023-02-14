# https://leetcode.cn/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i in range(len(nums)):
            if i > cover:
                return False
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
        return False


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))