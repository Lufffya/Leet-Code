# https://leetcode.cn/problems/minimum-path-sum/

from typing import List


### 官方解题 ###
# 思路: 先将边缘路径当前的结果计算出来, 在根据最小的总和选择下一步
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
            
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[rows - 1][columns - 1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))
