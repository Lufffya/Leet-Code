# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


### 初步设想 ###
# 思路: 依次记录每一个字符, 
# 如果字符不重复, 则叠加; 如果字符重复, 则设置为不记录;
# 最后得到 s 中所有的不重复的子字符串, 返回最长即可
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        s_dict = []
        for i in range(len(s)):
            for j in range(len(s_dict)):
                if s_dict[j][1] : continue
                if s[i] not in s_dict[j][0]:
                    s_dict[j][0] = s_dict[j][0] + s[i]
                else:
                    s_dict[j][1] = True
            s_dict.append([s[i], False])
        return max([len(i[0]) for i in s_dict])
### 结果 ### 
# 一个可行的想法, 但超出了运行时间限制...


### 进阶 ###
# 思路: 1, s_dict, 存储每一个字符的索引
# 2, max_len, 在每次循环中计算当前的最长子串长度, 用当前字符位置(i+1) - 当前字符之前不重复字符的起始索引(prev_i)
# 3, prev_i, 当遇到重复的字符时, 将 prev_i 设置为当前重复字符上一次出现时的索引
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        max_len, prev_i, s_dict = 0, 0, {}
        for i in range(len(s)):
            # 当发生重复时, prev_i 由重复字符上一次出现时的位置所以决定
            if s[i] in s_dict:
                # 这里的逻辑含义是: 当某个字符重复时, 将计算起始索引标记到上一个重复字符的索引
                # 因为重复字符之前的字符都是无效的 e.g: "abcdefgba", 当遇到第二个"b"时, 第一个字符"a"和第二个字符"b"都是无效的
                prev_i = max(s_dict[s[i]], prev_i)
            # 当不重复时, prev_i 永远为0, 依次计算((i + 1) - prev_i) 即可
            max_len = max(max_len, (i + 1) - prev_i)
            # 将当前字符的位置存入字典
            s_dict[s[i]] = i + 1
        return max_len
### 结果 ### 
# 执行用时: 64 ms, 在所有 Python3 提交中击败了 75.44% 的用户
# 内存消耗: 15.1 MB, 在所有 Python3 提交中击败了 45.46% 的用户


### Copilot ####
### 思路: Copilot 暴力解法, 遍历所有的字串组合情况, set去重判断是否相等
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) == j-i:
                    max_len = max(max_len, j-i)
        return max_len
### 结果 ### 
# 一个可行的想法, 但超出了运行时间限制...



### Copilot ####
### 思路: 调试完直接感叹, 又简单又还算高效的方法, 怎么就没想到呢...
# 定义两个指针 start, end, 分别表示子串的起始和结束位置, 从s的第一个字符开始, 分别向后移动指针, 直到找到不重复的字串
class Solution1:
    # Find the length of the longest substring in the string s that does not contain duplicate characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
            max_len = max(max_len, end - start)
        return max_len
### 结果 ### 
# 执行用时: 80 ms, 在所有 Python3 提交中击败了 38.79% 的用户
# 内存消耗: 15.2 MB, 在所有 Python3 提交中击败了 13.81% 的用户


if __name__ == '__main__':
    s = "abcdefba"
    print(Solution1().lengthOfLongestSubstring(s))
