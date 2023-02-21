# https://leetcode.cn/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        def backtrack(start_index, _sum):
            
            if _sum >= target:
                if _sum == target:
                    res.append(path[:])
                return

            for i in range(start_index, len(candidates)):

                if _sum + candidates[i] > target:
                    continue

                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                _sum += candidates[i]
                backtrack(i + 1, _sum)
                _sum -= candidates[i]
                path.pop()

        path = []
        res = []
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    candidates = [1,1,1,2]
    target = 3
    print(Solution().combinationSum2(candidates, target))