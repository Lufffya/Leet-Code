# https://leetcode.cn/problems/assign-cookies/

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        if len(s) == 0:
            return 0

        g.sort()
        s.sort()
        g = g[::-1]
        s = s[::-1]

        res = 0
        j = 0
        for i in range(len(g)):
            if j >= len(s):
                break
            if s[j] >= g[i]:
                res += 1
                j += 1
        return res



if __name__ == "__main__":
    g = [1,2,3]
    s = [3]
    print(Solution().findContentChildren(g, s))