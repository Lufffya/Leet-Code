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


### Copilot ###
# 思路: 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ''
        if len(s) == 1: return s
        start, max_len = 0, 1
        for i in range(len(s)):
            
            # 奇数回文向前取一个字符
            odd_part = s[i-max_len-1: i+1]
            
            if i-max_len >= 1 and odd_part == odd_part[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            
            even_part = s[i-max_len: i+1]
            if i-max_len >= 0 and even_part == even_part[::-1]:
                start = i-max_len
                max_len += 1
                
        return s[start:start + max_len]
### 结果 ### 
# 执行用时: 120 ms, 在所有 Python3 提交中击败了 98.80% 的用户
# 内存消耗: 15 MB, 在所有 Python3 提交中击败了 98.70% 的用户
            

if __name__ == "__main__":
    s = "abcdcbazzzabcdefgfedcba"
    print(Solution().longestPalindrome(s))
    
# 奇：
# 偶：
# 奇：
# 偶：cb
# 奇：cbb
# 偶：bb
# 奇：cbbd
# 偶：bbd
# bb

# 奇：
# 偶：   
# 奇：     
# 偶：ba   
# 奇：bab  
# 奇：     
# 偶：baba 
# 奇：babad
# 偶：abad 
# bab  


# 奇：
# 偶：
# 奇：
# 偶：ab
# 奇：abc
# 偶：  bc
# 奇：  bcd
# 偶：    cd
# 奇：    cdc
# 奇：   bcdcb
# 奇：abcdcba
# 奇：
# 偶：abcdcbaz
# 奇：abcdcbazz
# 偶：  bcdcbazz
# 奇：  bcdcbazzz
# 偶：    cdcbazzz
# 奇：    cdcbazzza
# 偶：      dcbazzza
# 奇：      dcbazzzab
# 偶：        cbazzzab
# 奇：        cbazzzabc 
# 奇：      dcbazzzabcd
# 奇：    cdcbazzzabcde
# 偶：      dcbazzzabcde
# 奇：      dcbazzzabcdef
# 偶：        cbazzzabcdef
# 奇：        cbazzzabcdefg
# 偶：          bazzzabcdefg
# 奇：          bazzzabcdefgf
# 偶：            azzzabcdefgf
# 奇：            azzzabcdefgfe
# 偶：             zzzabcdefgfe
# 奇：             zzzabcdefgfed
# 偶：               zzabcdefgfed
# 奇：               zzabcdefgfedc
# 偶：                zabcdefgfedc
# 奇：                zabcdefgfedcb
# 偶：                abcdefgfedcb
# 奇：                abcdefgfedcba
#  abcdefgfedcba