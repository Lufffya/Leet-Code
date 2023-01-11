# https://leetcode.cn/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0

        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for col in range(n):
            if obstacleGrid[0][col]:
                break
            else:
                dp[0][col] = 1

        for row in range(m):
            if obstacleGrid[row][0]:
                break
            else:
                dp[row][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    obstacleGrid = [[0,0],[1,0]]
    r = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(r)
