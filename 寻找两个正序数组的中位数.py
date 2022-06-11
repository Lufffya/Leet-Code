# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/


# 二分查找法
# def bin_search(data_list, val):    
#     low = 0                         # 最小数下标    
#     high = len(data_list) - 1       # 最大数下标    
#     while low <= high:        
#         mid = (low + high) // 2     # 中间数下标        
#         if data_list[mid] == val:   # 如果中间数下标等于val, 返回            
#             return mid        
#         elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标            
#             high = mid - 1        
#         else:                       # 如果val在中间数右边, 移动low下标            
#             low = mid + 1    
#     return # val不存在, 返回None


# arr = list(range(1, 10))

# ret = bin_search(arr, 3)
# print(ret)
    

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return float((nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2)
        else:
            return float(nums1[len(nums1) // 2])


if __name__ == "__main__":
    n1 = [1,3]
    n2 = [2]

    print(Solution().findMedianSortedArrays(n1, n2))