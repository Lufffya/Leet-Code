# https://leetcode.cn/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        row, col  = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[-1][-1] == 1:
            return 0
        
        if row == 1 or col == 1:
            return 0 if obstacleGrid[0][0] == 1 else 1
                
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        o = False
        for i in range(col):
            if not o:
                dp[0][i] = 1
                if obstacleGrid[0][i] == 1:
                    dp[0][i] = 0
                    o = True
            else:
                dp[0][i] = 0
        
        o = False
        for i in range(row):
            if not o:
                dp[i][0] = 1
                if obstacleGrid[i][0] == 1:
                    dp[i][0]  = 0
                    o = True
            else:
                dp[i][0]  = 0
        
        
        for i in range(1, row):
            for j in range(1, col):
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return dp[-1][-1]
    

if __name__ == "__main__":
    obstacleGrid = [[0,0],[1,1],[0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
    