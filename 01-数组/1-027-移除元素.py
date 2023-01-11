# https://leetcode.cn/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        if len(set(nums)) == 1:
            return 0 if nums[0] == val else len(nums)

        left = 0
        right = len(nums) - 1
        
        while left <= right:

            while left <= right and nums[left] != val:
                left += 1

            while left <= right and nums[right] == val:
                right -= 1
            
            if left < right and nums[left] == val:
                nums[left] = nums[right]

                left += 1
                right -= 1

        return left


if __name__ == '__main__':
    nums = [0,1,2,3,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))