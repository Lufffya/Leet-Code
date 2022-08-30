# https://leetcode.cn/problems/majority-element/

import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    nums = [3,2,3]
    print(Solution().majorityElement(nums))
