# https://leetcode.cn/problems/3sum-closest/

from typing import List


### 初步设想 ###
# 思路: 此题和15题思路大致相同, 只不过求和的目标值从0变成target
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            print(i, l, r)
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s == target:
                    return s
                
                if abs(s - target) < abs(res - target):
                    res = s
                    
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return res


if __name__ == "__main__":
    nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    target = 9999
    print(Solution().threeSumClosest(nums, target))
