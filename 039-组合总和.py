# https://leetcode.cn/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


### 官方解题 ###
# 思路: 搜索回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(target, combine, idx):
            if idx == len(candidates):
                return
            if target == 0:
                ans.append(combine)
                return

            # 直接跳过
            dfs(target, combine, idx + 1)
            # 选择当前数
            if target - candidates[idx] >= 0:
                dfs(target - candidates[idx], combine+[candidates[idx]], idx)
                
        dfs(target, [], 0)
        return ans
    

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
