# https://leetcode.cn/problems/non-decreasing-subsequences/

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start_index):
            
            if len(path) > 1:
                res.append(path[:])

            if start_index == len(nums):
                return

            usage = set()

            for i in range(start_index, len(nums)):
                
                if len(path) >= 1 and nums[i] < path[-1]:
                    continue
                
                if nums[i] in usage:
                    continue

                usage.add(nums[i])
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        path = []
        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [4,6,7,7]
    print(Solution().findSubsequences(nums))