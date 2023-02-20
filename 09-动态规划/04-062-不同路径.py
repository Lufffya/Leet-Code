# https://leetcode.cn/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[0] = [1] * n

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]  = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))