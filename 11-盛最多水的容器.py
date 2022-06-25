# https://leetcode.cn/problems/container-with-most-water/

from typing import List


### 初步设想 ####
### 创建双指针遍历所有组合可能, 暴力破解
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)): 
                max_area = max(max_area, abs(i - j) * min(height[i], height[j]))
        return max_area
### 结果 ### 
# 一个可行的想法, 但超出了运行时间限制...


### 进阶 ###
# 思路: 创建双指针, 从前后分别向中间靠拢遍历, 计算面积, 并且移动最小长度的指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
### 结果 ### 
# 执行用时: 232 ms, 在所有 Python3 提交中击败了 36.12% 的用户
# 内存消耗: 24.1 MB, 在所有 Python3 提交中击败了 97.35% 的用户


if __name__ == "__main__":
    height = [1,1]
    print(Solution().maxArea(height))
