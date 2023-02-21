# https://leetcode.cn/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for j in range(len(s) + 1):
            for word in wordDict:
                if j < len(word):
                    continue
                if dp[j - len(word)] and word == s[j - len(word): j]:
                    dp[j] = True
                
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))