# https://leetcode.cn/problems/candy/

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1
        
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candys[j] = max(candys[j], candys[j+1] + 1)

        return sum(candys)


if __name__ == "__main__":
    ratings = [1,0,2]
    print(Solution().candy(ratings))