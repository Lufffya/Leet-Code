# https://leetcode.cn/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        step = 0
        next_cover = 0
        cover = 0
        for i in range(len(nums)):
            next_cover = max(next_cover, i + nums[i])
            if i == cover:
                if cover != len(nums) - 1:
                    step += 1
                    cover = next_cover
                    if cover >= len(nums) - 1:
                        break
        return step


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))