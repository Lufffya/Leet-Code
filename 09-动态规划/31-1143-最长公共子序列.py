# https://leetcode.cn/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    res = max(res, dp[i][j])
                    
        return res
        
    
if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace" 
    print(Solution().longestCommonSubsequence(text1, text2))