# https://leetcode.cn/problems/implement-strstr/


### 初步设想 ###
# 思路: 没什么好做的
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))
