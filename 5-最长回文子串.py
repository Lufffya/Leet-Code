# https://leetcode-cn.com/problems/longest-palindromic-substring/


### 初步设想 ###
# 思路: 创建两个指针, 遍历查找所有的回文字符串, 取最长
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 0: return ''
#         if len(s) == 1: return s
#         p_max = ''
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 s_part =  s[i:j + 1]
#                 if s_part == s_part[::-1]:
#                     p_max = max(p_max, s_part, key=len)
#         return p_max
### 结果 ### 
# 一个可行的想法, 但超出了运行时间限制...


### 进阶 ###
# 思路: 
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 0: return ''
#         if len(s) == 1: return s
#         start = 0; end = 0
#         for i in range(len(s)):
#             s_part = s[i: len(s)]
            
            
            
            
        
        
### 结果 ### 
# 一个可行的想法, 但超出了运行时间限制...


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        if len(s) == 1: return s
        start = 0 # 起始的索引
        max_len = 1 # 最长的回文子串的长度, 当s大于1时, 初始值为1
        for i in range(len(s)):
            
            # 奇数回文
            odd_fragment = s[i - max_len - 1:i + 1]
            print('奇：' + odd_fragment)
            
            if i - max_len >= 1 and odd_fragment == odd_fragment[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
                
            # 偶数回文
            even_fragment = s[i - max_len:i + 1]
            print('偶：' + even_fragment)
            
            if i - max_len >= 0 and even_fragment == even_fragment[::-1]:
                start = i - max_len
                max_len += 1
                
        return s[start:start + max_len]



if __name__ == "__main__":
    
    # 输入：s = "babad"
    # 输出："bab"
    # 解释："aba" 同样是符合题意的答案。
    
    # 输入：s = "cbbd"
    # 输出："bb"
    
    s = "abcdcbazzzabcdefgfedcba"
    print(Solution().longestPalindrome(s))