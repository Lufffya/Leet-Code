# https://leetcode.cn/problems/queue-reconstruction-by-height/

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(Solution().reconstructQueue(people))