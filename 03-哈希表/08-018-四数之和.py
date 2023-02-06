# https://leetcode.cn/problems/4sum/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, nums_len):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = nums_len - 1

                while left < right:

                    _sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if _sum > target:
                        right -= 1
                    
                    elif _sum < target:
                        left += 1

                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        right -= 1
                        left += 1
        
        return res



if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))