# https://leetcode.cn/problems/container-with-most-water/

from typing import List


### 初步设想 ####
# 思路: 创建双指针遍历所有组合可能, 暴力破解
# 一个可行的想法, 但超出了运行时间限制...
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)): 
                max_area = max(max_area, abs(i - j) * min(height[i], height[j]))
        return max_area


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


if __name__ == "__main__":
    height = [1,1]
    print(Solution().maxArea(height))
