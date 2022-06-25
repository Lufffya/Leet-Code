# https://leetcode.cn/problems/integer-to-roman/


### 初步设想 ###
# 思路: 列出罗马数字的所有组合形式, 从大到小遍历依次判断被减条件, 将转换的字符累加
class Solution:
    def intToRoman(self, num: int) -> str:
        characters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values     = [1000, 900, 500, 400,  100,  90,   50,  40,   10,   9,   5,    4,   1]
        roman = ''
        while num != 0:
            for i in range(len(characters)):
                if num >= values[i]:
                    num -= values[i]
                    roman += characters[i]
                    break
        return roman
### 结果 ### 
# 执行用时: 60 ms, 在所有 Python3 提交中击败了 19.57% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 86.17% 的用户


### Copilot ###
# 思路: 排序还是自己加上去的。。。
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        res = ''
        for k, v in dict(sorted(roman.items(), key=lambda x : x[0], reverse=True)).items():
            while num >= k:
                res += v
                num -= k
        return res
### 结果 ### 
# 执行用时: 60 ms, 在所有 Python3 提交中击败了 19.57% 的用户
# 内存消耗: 14.9 MB, 在所有 Python3 提交中击败了 86.17% 的用户

if __name__ == "__main__":
    num = 9
    print(Solution().intToRoman(num))
