# https://leetcode.cn/problems/maximum-subarray/

from typing import List


### 大神解题 ###
# 思路: 每一步都计算前一时刻的累计和, 如果大于0, 证明对后续数组有正向作用
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0
        for i in range(len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res, sum)
        
        return res


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
    