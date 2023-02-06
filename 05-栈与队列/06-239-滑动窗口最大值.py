# https://leetcode.cn/problems/sliding-window-maximum/

from collections import deque
from typing import List

class MyQueue:
    def __init__(self):
        self.queue = deque()
    
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        que = MyQueue()

        for i in range(k):
            que.push(nums[i])
        res.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            res.append(que.front())
        return res


if __name__ == '__main__':
    nums = [1,3,-1,0,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))