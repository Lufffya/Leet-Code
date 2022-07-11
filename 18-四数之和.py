# https://leetcode.cn/problems/4sum/

from typing import List


### 初步设想 ###
# 思路: 这题和15题-三数之和一样, 只是多了一层循环, 剩下的两层还是延续之前排序后双指针的思路
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1    
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1    
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
### 结果 ### 
# 执行用时: 1118 ms, 在所有 Python3 提交中击败了 22.49% 的用户
# 内存消耗: 15 MB, 在所有 Python3 提交中击败了 47.46% 的用户


### Copilot ###
# 思路: 思路一致, 只是在当sum的结果不一致时, 没有用到左右指针取值筛选重复的操作, 反而执行时间还更短了
# 猜想可能是去重本来就是一个耗时的操作, 但是对结果居然没有影响
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
### 结果 ### 
# 执行用时: 808 ms, 在所有 Python3 提交中击败了 51.67% 的用户
# 内存消耗: 14.8 MB, 在所有 Python3 提交中击败了 97.62% 的用户


if __name__ == "__main__":
    nums = [2,2,2,2,2]
    target = 8
    print(Solution().fourSum(nums, target))
