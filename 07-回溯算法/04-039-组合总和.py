# https://leetcode.cn/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start_index, _sum):
            
            if _sum >= target:
                if _sum == target:
                    res.append(path[:])
                return

            for i in range(start_index, len(candidates)):
                if _sum + candidates[i] > target:
                    continue
                path.append(candidates[i])
                _sum += candidates[i]
                backtrack(i, _sum)
                _sum -= candidates[i]
                path.pop()

        path = []
        res = []
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))