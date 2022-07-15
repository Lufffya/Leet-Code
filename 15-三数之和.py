# https://leetcode.cn/problems/3sum/

from typing import List


### 官方思路 ###
# 思路: 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans


### Copilot ###
# 思路: 三重循环的优化版, 首先排序nums, 避免重复, 以及方便双指针的遍历, 
# 在第一重循环下创建左右双指针, 向中间遍历逼近, 
# 当和小于0时, 左指针向右移动, 当和大于0时, 右指针向左移动, 此过程直到满足和为0,
# 当满足条件时, 记录该三元组的组合, 并且左右指针向中间靠拢一个下标, 继续遍历,
# 值得注意的时, 为了避免重复的三元组, 需要用While循环来分别找到左右指针指向不重复的目标值, 第一重循环的IF判断也是为了这个目的.
# 这个思路更官方的解题思路差不多, 但是总感觉要更简单一点
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))
