# https://leetcode.cn/problems/string-to-integer-atoi/


### 初步设想 ###
# 思路: 
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '': return 0
        s_p =  s[0] if s[0] in ['-', '+'] else ''
        s = s[1:] if s_p else s
        if s == '' or not s[0].isdigit() : return 0
        new_s = ''
        for _s in s:
            if _s.isdigit(): new_s += _s
            else : break
        s = int(s_p + new_s)
        if s >= 2**31-1: s = 2**31-1
        elif s <= -2**31: s = -2**31
        return s


if __name__ == "__main__":
    s = "-"
    print(Solution().myAtoi(s))
