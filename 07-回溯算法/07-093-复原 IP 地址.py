# https://leetcode.cn/problems/restore-ip-addresses/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtrack(start_index):
            
            if len(path) == 4:
                if len(''.join(path)) == len(s):
                    res.append('.'.join(path))
                return

            for i in range(start_index, len(s)):
                p_s = s[start_index:i + 1]
                
                if p_s[0] == '0' and len(p_s) > 1:
                    break
                if int(p_s) > 255:
                    break

                path.append(p_s)
                backtrack(i + 1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    s = "101023"
    print(Solution().restoreIpAddresses(s))