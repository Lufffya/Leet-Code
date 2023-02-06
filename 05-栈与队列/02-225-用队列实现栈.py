# https://leetcode.cn/problems/implement-stack-using-queues/

from collections import deque


class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        
        return self.queue_out.popleft()

    def top(self) -> int:
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0


if __name__ == '__main__':
    myStack = MyStack()

    methods = ['MyStack','push','push','top','pop','empty']
    vales = [[],[1],[2],[],[],[]]
    
    for m, v in zip(methods[1:], vales[1:]):
        if m == 'push':
            myStack.push(v[0])
        elif m == 'pop':
            myStack.pop()
        elif m == 'top':
            myStack.top()
        elif m == 'empty':
            myStack.empty()