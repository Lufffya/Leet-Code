# https://leetcode.cn/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(n):
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n = n // 10
            return _sum
        
        vals = []

        while True:
            n = get_sum(n)

            if n == 1:
                return True

            if n in vals:
                return False
            vals.append(n)


if __name__ == "__main__":
    n = 19
    print(Solution().isHappy(n))