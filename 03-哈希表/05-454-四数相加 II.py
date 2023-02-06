# https://leetcode.cn/problems/4sum-ii/

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        val_dict = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in val_dict:
                    val_dict[n1 + n2] += 1
                else:
                    val_dict[n1 + n2] = 1

        res = 0
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in val_dict:
                    res += val_dict[-(n3 + n4)]

        return res


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(Solution().fourSumCount(nums1, nums2, nums3, nums4))