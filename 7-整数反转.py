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
### 结果 ### 
# 执行用时: 40 ms, 在所有 Python3 提交中击败了 58.33% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 36.67% 的用户


if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
