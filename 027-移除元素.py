# https://leetcode.cn/problems/remove-element/

from typing import List


### 初步设想 ###
# 思路: 删除
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            i -= count
            if nums[i] == val:
                nums.pop(i)
                count += 1
        return len(nums)


### 初步设想2 ###
# 思路: 移动
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(set(nums)) == 1 and nums[0] == val:
            nums.clear()
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                i -= 1
            i += 1
        return j + 1


### Copilot ###
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == "__main__":
    nums = [1,2,3,3,4,5,3,3,6]
    val = 3
    print(Solution().removeElement(nums, val))
