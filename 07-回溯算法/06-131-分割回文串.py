# https://leetcode.cn/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(start_index):

            if start_index == len(s):
                res.append(path[:])
                return

            for i in range(start_index, len(s)):
                p_s = s[start_index:i + 1]
                if p_s != p_s[::-1]:
                    continue
                path.append(p_s)
                backtrack(i + 1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))