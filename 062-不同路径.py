# https://leetcode.cn/problems/unique-paths/


### 官方解题 ###
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 7
    print(Solution().uniquePaths(m, n))