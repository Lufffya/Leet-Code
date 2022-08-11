# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from  typing import List


### 初步设想 ###
# 思路: 二分查找, 但是感觉时间复杂度不是o(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = r = mid
                while l != 0 and nums[l - 1] == target:
                    l -= 1
                while r != len(nums) - 1 and nums[r + 1] == target:
                    r += 1
                return [l, r]
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target :
                r = mid - 1
        return [-1, -1]


if __name__ == "__main__":
    nums = [0,1,2,3,4,4,4]
    target = 2
    print(Solution().searchRange(nums, target))
