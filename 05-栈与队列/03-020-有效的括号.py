# https://leetcode.cn/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(')')
            
            elif s[i] == '[':
                stack.append(']')
            
            elif s[i] == '{':
                stack.append('}')

            elif not stack or stack[-1] != s[i]:
                return False
            else:
                stack.pop()

        return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    print(Solution().isValid(s))
