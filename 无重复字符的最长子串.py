# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        max_len, prev_i, s_dict = 0, 0, {} 
        for i in range(len(s)):
            if s[i] in s_dict:
                prev_i = max(s_dict[s[i]], prev_i)
            
            max_len = max(max_len, (i + 1) - prev_i)
            
            s_dict[s[i]] = i + 1
            
        return max_len
            
            
if __name__ == '__main__':
    
    # val = "abcabcbb"
    # val = "bbbbb"
    # val = "pwwkew"
    # val = " "
    # val = "au"
    val = "abba"

    print(Solution().lengthOfLongestSubstring(val))