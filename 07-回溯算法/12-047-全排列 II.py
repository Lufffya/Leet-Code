# https://leetcode.cn/problems/permutations-ii/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums):
            
            if len(nums) == 0:
                res.append(path[:])
                return

            usage = set()

            for n in nums:
                if n in usage:
                    continue
                
                usage.add(n)
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
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))