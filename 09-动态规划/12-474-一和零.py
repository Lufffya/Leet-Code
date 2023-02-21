# https://leetcode.cn/problems/ones-and-zeroes/

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zero, one = s.count('0'), s.count('1')
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1) 

        return dp[m][n]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 3
    n = 3
    print(Solution().findMaxForm(strs, m, n))