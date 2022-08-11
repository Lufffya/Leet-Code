# https://leetcode.cn/problems/powx-n/


### 官方解题 ###
# 思路: 快速幂 + 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


### 官方解题 ###
# 思路: 快速幂 + 迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


### Copilot ###
# 思路: 说实话, 代码看起来很简单
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)
    

if __name__ == "__main__":
    
    def fact(n):
        if n==1:
            return 1
        return n * fact(n - 1)
    # ===> fact(5)
    # ===> 5 * fact(4)
    # ===> 5 * (4 * fact(3))
    # ===> 5 * (4 * (3 * fact(2)))
    # ===> 5 * (4 * (3 * (2 * fact(1))))
    # ===> 5 * (4 * (3 * (2 * 1)))
    # ===> 5 * (4 * (3 * 2))
    # ===> 5 * (4 * 6)
    # ===> 5 * 24
    # ===> 120
    
    def fact2(num, product):
        if num == 1:
            return product
        return fact2(num - 1, num * product)
    # ===> fact2(5, 1)
    # ===> fact2(4, 5)
    # ===> fact2(3, 20)
    # ===> fact2(2, 60)
    # ===> fact2(1, 120)
    # ===> 120
    
    x = 2
    n = 4
    print(Solution().myPow(x, n))
