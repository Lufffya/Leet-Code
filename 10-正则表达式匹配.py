# https://leetcode.cn/problems/regular-expression-matching/submissions/


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
                                char = _part[0]
                                next_part = _part
                                break
                        
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
                    s = s[len(part):]
                else:
                    if s[:len(part)] == part:
                        s = s[len(part):]
                    else: return False
        if s != '': return False
        return True
        
        


if __name__ == "__main__":
    # s = 'aaa'
    # p = 'ab*a*c*a'
    s = 'aaca'
    p = 'ab*a*c*a'
    # s = 'a'
    # p = 'ab*'
    # s = 'bbbba'
    # p = '.*a*a'
    print(Solution().isMatch(s, p))
