# https://leetcode.cn/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start_index):
            
            res.append(path[:])

            if start_index == len(nums):
                return

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))