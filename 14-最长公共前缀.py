# https://leetcode.cn/problems/longest-common-prefix/

from typing import List


### 初步设想 ###
# 思路: 先从strs找到一个最短的字符, 因为它最大也只可能试最长的前缀; 
# 以最短的字符串为参照, 循环判断是否存在相同的前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        min_char = min(strs, key=len)
        for i in range(len(min_char)):
            for j in range(len(strs)):
                if strs[j][i] != min_char[i]:
                    return min_char[:i]
        return min_char
### 结果 ### 
# 执行用时: 36 ms, 在所有 Python3 提交中击败了 80.14% 的用户
# 内存消耗: 15.1 MB, 在所有 Python3 提交中击败了 30.08% 的用户


### Copilot ###
# 思路: 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        res = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[:-1]
        return res
### 结果 ### 
# 执行用时: 32 ms, 在所有 Python3 提交中击败了 93.41% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 99.41% 的用户


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))
