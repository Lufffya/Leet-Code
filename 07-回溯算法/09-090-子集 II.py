# https://leetcode.cn/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        def backtrack(start_index):
            
            res.append(path[:])

            if start_index == len(nums):
                return

            for i in range(start_index, len(nums)):

                if i > start_index and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))