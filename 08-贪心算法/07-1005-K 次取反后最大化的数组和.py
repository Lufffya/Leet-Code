# https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key= lambda x: abs(x), reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            if k == 0:
                break 
        
        if k > 0:
            nums.sort()
            while k > 0:
                nums[0] = -nums[0]
                k -= 1

        return sum(nums)


if __name__ == "__main__":
    nums = [-2,9,9,8,4]
    k = 5
    print(Solution().largestSumAfterKNegations(nums, k))