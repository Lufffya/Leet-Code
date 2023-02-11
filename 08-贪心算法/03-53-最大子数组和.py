# https://leetcode.cn/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]

            if count > res:
                res = count
            
            if count <= 0:
                count = 0

        return res


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))