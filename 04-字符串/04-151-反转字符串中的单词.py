# https://leetcode.cn/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])        


if __name__ == "__main__":
    s = "the sky is blue"
    print(Solution().reverseWords(s))