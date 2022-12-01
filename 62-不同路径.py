# https://leetcode.cn/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        dp[0] = [1] * n
        for row in range(m): dp[row][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 7
    r = Solution().uniquePaths(m, n)
    print(r)
