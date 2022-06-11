# https://leetcode-cn.com/problems/longest-palindromic-substring/




class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        if len(s) == 1: return s
        start = 0 # 起始的索引
        max_len = 1 # 最长的回文子串的长度, 当s大于1时, 初始值为1
        for i in range(len(s)):
            
            # 奇数回文
            odd_fragment = s[i - max_len - 1:i + 1]
            
            if i - max_len >= 1 and odd_fragment == odd_fragment[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
                
            # 偶数回文
            even_fragment = s[i - max_len:i + 1]
            
            if i - max_len >= 0 and even_fragment == even_fragment[::-1]:
                start = i - max_len
                max_len += 1
                
        return s[start:start + max_len]

    
    def longestPalindrome2(self, s: str) -> str:
        if len(s) == 0: return ""
        if len(s) == 1: return s
        palindrome_list = []
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    palindrome_list.append(s[i:j + 1])
        return max(palindrome_list, key=len)



if __name__ == "__main__":
    
    # 输入：s = "babad"
    # 输出："bab"
    # 解释："aba" 同样是符合题意的答案。
    
    # 输入：s = "cbbd"
    # 输出："bb"
    
    s = "abcdcbazzzabcdefgfedcba"
    print(Solution().longestPalindrome(s))