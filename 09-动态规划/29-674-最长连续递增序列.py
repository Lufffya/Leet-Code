# https://leetcode.cn/problems/longest-continuous-increasing-subsequence/


from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                    
        return max(dp)


if __name__ == '__main__':
    nums = [1,3,5,4,2,3,4,5]
    print(Solution().findLengthOfLCIS(nums))