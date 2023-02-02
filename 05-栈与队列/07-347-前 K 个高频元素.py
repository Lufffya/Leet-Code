# https://leetcode.cn/problems/top-k-frequent-elements/

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_dict = {}
        for i in range(len(nums)):
            if nums[i] in val_dict:
                val_dict[nums[i]] = val_dict[nums[i]] + 1
            else:
                val_dict[nums[i]] = 1

        pri_heapq = []

        for key, value in val_dict.items():
            heapq.heappush(pri_heapq, (value, key))
            if len(pri_heapq) > k:
                heapq.heappop(pri_heapq)

        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(pri_heapq)[1]
        return res


if __name__ == '__main__':
    nums = [1,1,1,1,6,2,2,2,3,3,4,5]
    k = 2
    print(Solution().topKFrequent(nums, k))