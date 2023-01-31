# https://leetcode.cn/problems/repeated-substring-pattern/comments/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


if __name__ == "__main__":
    s = "ababc"
    print(Solution().repeatedSubstringPattern(s))
