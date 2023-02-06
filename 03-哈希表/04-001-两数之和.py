# https://leetcode.cn/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_dict = {}
        for i, n in enumerate(nums):
            if n in val_dict:
                return [val_dict[n], i]
            else:
                val_dict[target - n] = i


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))