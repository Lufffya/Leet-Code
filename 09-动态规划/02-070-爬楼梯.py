# https://leetcode.cn/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]


class Solution:
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1
        m = 2

        for j in range(n + 1):
            for i in range(1, m + 1):
                if i > j:
                    continue
                dp[j] += dp[j - i]

        return dp[-1]


if __name__ == "__main__":
    n = 2
    print(Solution().climbStairs2(n))