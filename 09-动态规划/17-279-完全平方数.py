# https://leetcode.cn/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n + 1):
            sq = i * i
            for j in range(sq, n + 1):
                dp[j] = min(dp[j], dp[j - sq] + 1)

        return dp[-1]


if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n))