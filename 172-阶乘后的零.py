# https://leetcode.cn/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            print(i)
            while i % 5 == 0:
                i //= 5
                ans += 1
                print('+5')
        return ans


if __name__ == "__main__":
    n = 100
    print(Solution().trailingZeroes(n))