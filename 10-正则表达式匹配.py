# https://leetcode.cn/problems/regular-expression-matching/submissions/


### 初步设想 ###
# 思路: 已经捋不清楚了
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '.' not in p and '*' not in p:
            if s == p : return True
            else: return False
        p_list = []
        p_split = p.split('*')
        for i, part in enumerate(p_split):
            if part == '': continue
            if i + 1 == len(p_split):
                p_list.append(part)
                break
            p1 = part[:-1]
            p2 = part[-1] + '*'
            if p1 != '': 
                p_list.append(p1)
            p_list.append(p2)
        for i, part in enumerate(p_list):
            if '*' in part:
                perfix_i = 0
                perfix = part[0]
                if perfix == '.':
                    if i + 1 == len(p_list):
                        s = ''
                    else:
                        char = ''
                        char_num = 0
                        next_part = ''
                        max_part_i = 0
                        for _part in p_list[i+1:]:
                            if _part == '.*':
                                continue
                            elif _part[0] == '.':
                                for _p in _part:
                                    if _p == '.':
                                        char_num += 1
                                    else:
                                        char = _p
                                        next_part = _part
                                        break
                            else:
                                if i + 1 == len(p_list) - 1:
                                    for s_i in range(len(s)):
                                        if _part == s[s_i:s_i+len(_part)]:
                                            max_part_i = s_i
                                if max_part_i == 0 :
                                    char = _part[0]
                                    next_part = _part
                                    break
                                else :
                                    perfix_i = max_part_i
                                    break
                        if max_part_i == 0:
                            for _s in s:
                                if _s == char:
                                    break
                                perfix_i += 1
                        perfix_i -= char_num
                else:
                    if s == '': continue
                    if perfix == s[0]:
                        # if len(s) >= 2 and s[0] == s[1]:
                        # if len(s) >= 2 and len(list(set(s[:2]))) == 1:
                        if not (len(s) >= 2 and s[0] != s[1] and (i + 1 < len(p_list)) and '*' in p_list[i+1] and p_list[i+1][0] == s[1]):
                            out = False
                            for _part in p_list[i+1:]:
                                if '*' in _part :
                                    continue
                                else:
                                    for _p in _part:
                                        if perfix == _p or perfix == '.':
                                            perfix_i -= 1
                                        else: 
                                            out = True
                                            break
                                if out: break
                        for _s in s:
                            if _s == perfix:
                                perfix_i += 1
                            else: break
                    else:
                        pass
                s = s[perfix_i:]
            else:
                if '.' in part:
                    if len(s[:len(part)]) == len(part):
                        for i in range(len(s[:len(part)])):
                            if part[i] != '.' and part[i] != s[:len(part)][i]:
                                return False
                        s = s[len(part):]
                    else: return False
                    # if len(part) > len(s): return False
                    # s = s[len(part):]
                else:
                    if s[:len(part)] == part:
                        s = s[len(part):]
                    else: return False
        if s != '': return False
        return True
### 结果 ### 
# 没写出来, 差最后几个没调试好, 但是一开始的思路就是错的, 直接被github copilot 降维打击


### Copilot ###
# 思路: 
class Solution:
    # Give you a string s and a character rule P, implement a support'.' Match regular expression of '*', '.' Match any single character, '*' matches zero or more preceding elements
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    s ="aabcbcbcaccbcaabc"
    p =".*a*aa*.*b*.c*.*a*"
    print(Solution().isMatch(s, p))
