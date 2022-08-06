# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import List


### 初步设想 ###
# 思路: 将对应数字的字符循环累加
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return res
        D = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for i in range(len(digits)):
            if res == []:
                res = list(D[digits[i]])
                continue
            tmp = []
            for j in range(len(res)):
                for k in D[digits[i]]:
                    tmp.append(res[j] + k)
            res = tmp      
        return res


### Copilot ###
# 思路: 什么叫做优雅的代码?
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        for i in digits:
            res = [x + y for x in res for y in d[i]]
        return res


if __name__ == "__main__":
    digits = "234"
    print(Solution().letterCombinations(digits))
