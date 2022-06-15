# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/


from typing import List


### Copilot ###
# 思路: 合并并排序数组, 直接计算中位数
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return float((nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2)
        else:
            return float(nums1[len(nums1) // 2])
### 结果 ### 
# 执行用时: 36 ms, 在所有 Python3 提交中击败了 98.09% 的用户
# 内存消耗: 15.2 MB, 在所有 Python3 提交中击败了 19.33% 的用户


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2, 5]
    print(Solution().findMedianSortedArrays(nums1, nums2))
