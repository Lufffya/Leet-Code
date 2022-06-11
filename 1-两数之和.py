# https://leetcode.cn/problems/two-sum/


from typing import List


### 初步设想 ###
# 思路: 创建两个指针, 分别遍历nums, 判断跳过自我相加
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j : continue
                if (nums[i] + nums[j]) == target:
                    return [i, j]
### 结果 ### 
# 执行用时: 7780 ms, 在所有 Python3 提交中击败了 5.00% 的用户
# 内存消耗: 15.5 MB, 在所有 Python3 提交中击败了 91.52% 的用户


### Copilot ###
# 思路：创建一个字典, 循环存储nums中的数字和下标, 判断target减去当前数字是否在字典中
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
        return []
### 结果 ### 
# 执行用时: 40 ms, 在所有 Python3 提交中击败了 77.42% 的用户
# 内存消耗: 16.1 MB, 在所有 Python3 提交中击败了 29.56% 的用户


if __name__ == '__main__':
    nums = [2,5,5,11]
    target = 10
    print(Solution().twoSum(nums, target))
