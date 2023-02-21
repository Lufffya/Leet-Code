# https://leetcode.cn/problems/wiggle-subsequence/

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(set(nums)) == 1:
            return 1

        res = 1
        pre_diff = 0

        for i in range(len(nums) - 1):
            
            diff = nums[i + 1] - nums[i]
            
            if diff * pre_diff <= 0 and diff != 0:
                res += 1
                pre_diff = diff

        return res 


if __name__ == "__main__":
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(Solution().wiggleMaxLength(nums))