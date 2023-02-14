# https://leetcode.cn/problems/lemonade-change/

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            else:
                change = 15
                while change > 0:
                    if ten > 0:
                        ten -= 1
                        change -= 10
                    if five > 0:
                        five -= 1
                        change -= 5

                    if change > 0 and five == 0:
                        return False
        return True


if __name__ == "__main__":
    bills = [5,5,5,10,20]
    print(Solution().lemonadeChange(bills))