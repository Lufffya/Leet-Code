# https://leetcode.cn/problems/remove-element/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        new_nums = [0] * len(nums)
        max_index = right

        while left <= right:

            if nums[left] ** 2 > nums[right] ** 2:
                new_nums[max_index] = nums[left] ** 2
                max_index -= 1
                left += 1
            else:
                new_nums[max_index] = nums[right] ** 2
                max_index -= 1
                right -= 1
        
        return new_nums



if __name__ == "__main__":
    nums = [-7,-3,2,3,11]
    print(Solution().sortedSquares(nums))