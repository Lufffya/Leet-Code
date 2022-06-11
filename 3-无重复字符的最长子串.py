# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


### 初步设想 ###
# 思路: 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        s_dict = []
        for i in range(len(s)):
            for j in range(len(s_dict)):
                if s_dict[j][0] != s[i]:
                    s_dict[j] = s_dict[j] + s[i]
            s_dict.append(s[i])
        return max(s_dict)
        
        
        
        

### 结果 ### 
# 执行用时: 72 ms, 在所有 Python3 提交中击败了 18.15% 的用户
# 内存消耗: 15 MB, 在所有 Python3 提交中击败了 43.29% 的用户


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    
    
    
    
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0: return 0
#         if len(s) == 1: return 1
#         max_len, prev_i, s_dict = 0, 0, {}
#         for i in range(len(s)):
#             if s[i] in s_dict:
#                 prev_i = max(s_dict[s[i]], prev_i)
            
#             max_len = max(max_len, (i + 1) - prev_i)
            
#             s_dict[s[i]] = i + 1
            
#         return max_len