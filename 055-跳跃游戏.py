# https://leetcode.cn/problems/jump-game/

from typing import List


### 官方解题 ###
# 思路: 每次都计算能到达的最长距离, 一旦当前索引大于最长距离, 则证明不能到达
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))