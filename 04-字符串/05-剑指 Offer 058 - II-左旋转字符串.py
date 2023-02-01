# https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

if __name__ == "__main__":
    s = "abcdefg"
    n = 2
    print(Solution().reverseLeftWords(s, n))