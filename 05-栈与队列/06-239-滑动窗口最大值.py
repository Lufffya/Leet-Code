# https://leetcode.cn/problems/sliding-window-maximum/

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(len(nums)):

            queue.append(nums[i])

            if i > 0 and nums[i] > queue[0]:
                queue.popleft()

            w = nums[i:i+k]
            if len(w) != k:
                break
            res.append(max(w))
        return res


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]

    s = deque()

    for a in nums:
        s.append(a)
    
    print(s.popleft())


    k = 3
    print(Solution().maxSlidingWindow(nums, k))
