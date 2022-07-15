#https://leetcode.cn/problems/palindrome-number/


### 初步设想 ###
# 思路: 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))
