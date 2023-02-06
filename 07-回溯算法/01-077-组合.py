# https://leetcode.cn/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start_index):
            
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(start_index, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()

        path = []
        res = []
        backtrack(1)
        return res



if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n, k))