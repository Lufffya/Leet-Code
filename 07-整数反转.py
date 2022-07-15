# https://leetcode.cn/problems/reverse-integer/


### 初步设想 ###
# 思路: 
class Solution:
    def reverse(self, x: int) -> int:
        x_s = str(x)
        x_p = '-' not in x_s
        x_s = x_s.replace('-', '')
        x_i = x_s[::-1]
        return int(('' if x_p else '-') + x_i) if -2**31<int(x_i)<2**31-1 else 0


### Copilot ###
# 思路: 
class Solution:
    # Give you a 32-bit signed integer x, and return the result after reversing the number part in X.
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 0:
            x = -x
            x = int(str(x)[::-1])
            x = -x
        else:
            x = int(str(x)[::-1])
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x


if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
