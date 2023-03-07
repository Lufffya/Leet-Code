# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                    
        return res


if __name__ == '__main__':
    nums2 = [1,2,3,2,1]
    nums1 = [3,2,1,4,7]
    print(Solution().findLength(nums1, nums2))