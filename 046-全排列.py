# https://leetcode.cn/problems/permutations/

from typing import List


### 初步设想 ###
# 思路: 回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, res):
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                backtrack(path + [nums[i]], res)
        res = []
        backtrack([], res)
        return res


### Copilot ###
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        res = []
        backtrack(nums, [])
        return res
        
   
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
