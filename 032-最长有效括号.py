# https://leetcode.cn/problems/longest-valid-parentheses/


### 官方解题 ###
# 思路: 堆栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


### 官方解题 ###
# 思路: 
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        for _s in s:
            if _s == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left + right)
            if right > left:
                left, right = 0, 0
        left, right = 0, 0
        for _s in s[::-1]:
            if _s == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left + right)
            if right < left:
                left, right = 0, 0
        return ans


### Copilot ###
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + dp[i - 2]
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == "__main__":
    s = "(()())"
    print(Solution().longestValidParentheses(s))
