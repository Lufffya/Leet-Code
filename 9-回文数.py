#https://leetcode.cn/problems/palindrome-number/


### 初步设想 ###
# 思路: 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
### 结果 ### 
# 执行用时: 28 ms, 在所有 Python3 提交中击败了 99.53% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 87.54% 的用户


if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))
