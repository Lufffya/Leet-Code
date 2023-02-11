# https://leetcode.cn/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums):
            
            if len(nums) == 0:
                res.append(path[:])
                return

            for n in nums:
                path.append(n)
                
                _nums = nums[:]
                _nums.remove(n)

                backtrack(_nums)
                path.pop()

        path = []
        res = []
        backtrack(nums)
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))