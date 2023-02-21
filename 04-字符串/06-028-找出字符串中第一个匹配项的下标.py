# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        pre_fix = [0] * m
        for i in range(1, m):
            j = pre_fix[i - 1]
            while j > 0 and needle[i] != needle[j]:
                j = pre_fix[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pre_fix[i] = j
                 
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = pre_fix[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("aabaabaafa ", "aabaaf"))