# https://leetcode.cn/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        n = self.pop()
        self.stack_out.append(n)
        return n

    def empty(self) -> bool:
        return len(self.stack_in) == 0 and len(self.stack_out) == 0


if __name__ == '__main__':
    myQueue = MyQueue()

    methods = ['MyQueue','push','push','push','push','pop','push','pop','pop','pop','pop']
    vales = [[],[1],[2],[3],[4],[],[5],[],[],[],[]]
    
    for m, v in zip(methods[1:], vales[1:]):
        if m == 'push':
            myQueue.push(v[0])
        elif m == 'pop':
            myQueue.pop()
        elif m == 'peek':
            myQueue.peek()
        elif m == 'empty':
            myQueue.empty()
