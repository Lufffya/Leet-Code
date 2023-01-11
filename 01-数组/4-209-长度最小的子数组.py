# https://leetcode.cn/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        i = 0
        sums = 0
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= target:
                min_len = min(min_len, (j+1)-i)
                sums -= nums[i]
                i += 1
        return 0 if min_len == float('inf') else min_len

        
if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    print(Solution().minSubArrayLen(target, nums))
