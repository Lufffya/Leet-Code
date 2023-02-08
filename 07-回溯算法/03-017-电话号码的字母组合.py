# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            
            if index == len(digits):
                res.append(''.join(path))
                return

            letters = phone[digits[index]]
            for i in range(len(letters)):
                path.append(letters[i]) 
                backtrack(index + 1)
                path.pop()

        if not digits:
            return []

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    digits = "23"
    print(Solution().letterCombinations(digits))