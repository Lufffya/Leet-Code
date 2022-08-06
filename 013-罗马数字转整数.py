# https://leetcode.cn/problems/roman-to-integer/


### 初步设想 ###
# 思路: 和整数转罗马数字一个套路
class Solution:
    def romanToInt(self, s: str) -> int:
        characters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values     = [1000, 900, 500, 400,  100,  90,   50,  40,   10,   9,   5,    4,   1]
        _int = 0
        while s != '':
            for i in range(len(characters)):
                if s.startswith(characters[i]):
                    _int += values[i]
                    s = s[len(characters[i]):]
                    break
        return _int


### Copilot ###
# 思路: 
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                res += roman_dict[s[i]]
            elif roman_dict[s[i]] < roman_dict[s[i + 1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        return res


if __name__ == "__main__":
    s = "III"
    print(Solution().romanToInt(s))
