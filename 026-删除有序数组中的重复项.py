# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

from typing import List


### 初步设想 ###
# 思路: 判断 i 是否等于 i-1, 如果是则删除 i
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(len(nums)):
            i -= count
            if i != 0 and nums[i] == nums[i-1]:
                nums.pop(i)
                count += 1
        return len(nums)


### Copilot ###
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


### 官方解题 ###
# 思路: 和 Copilot 异曲同工
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
