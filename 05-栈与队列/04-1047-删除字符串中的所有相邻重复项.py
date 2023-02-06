# https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if i > 0 and stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)


if __name__ == '__main__':
    s = 'abbaca'
    print(Solution().removeDuplicates(s))