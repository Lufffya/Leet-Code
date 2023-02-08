# https://leetcode.cn/problems/combination-sum-iii/

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(start_index):
            
            if len(path) == k:
                if sum(path) == n:
                    res.append(path[:])
                return
            
            for i in range(start_index, 10-(k-len(path))+1):
                path.append(i)
                backtrack(i+1)
                path.pop()

        path = []
        res = []
        backtrack(1)
        return res


if __name__ == "__main__":
    k = 9
    n = 45
    print(Solution().combinationSum3(k, n))