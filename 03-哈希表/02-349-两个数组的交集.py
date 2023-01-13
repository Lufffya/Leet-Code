#  https://leetcode.cn/problems/intersection-of-two-arrays/

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_dict = {}
        res = []
        for n in nums1:
            if n not in val_dict:
                val_dict[n] = 1
        for n in nums2:
            if n in val_dict.keys() and val_dict[n] == 1:
                res.append(n)
                val_dict[n] = -1

        return res


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    s = Solution().intersection()
