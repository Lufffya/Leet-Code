# https://leetcode.cn/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 0
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i],  max(j * (i-j), j * dp[i-j]))

        return dp[-1]


if __name__ == "__main__":
    n = 10
    print(Solution().integerBreak(n))