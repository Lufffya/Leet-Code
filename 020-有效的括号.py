# https://leetcode.cn/problems/valid-parentheses/


### 初步设想 ###
# 思路: 灵机一动就想出来了嘿嘿
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''


### 官方思路 ###
# 思路: 感觉很优雅
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        D = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in D:
                if not stack or stack.pop() != D[c]:
                    return False
            else:
                stack.append(c)
        return not stack


### Copilot ###
# 思路: 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = "()"
    print(Solution().isValid(s))
