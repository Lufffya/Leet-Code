# https://leetcode.cn/problems/search-in-rotated-sorted-array/

from typing import List


### Copilot ###
# 思路: 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))
