class MyQueue:

    def __init__(self):
        self.queue = list()
        self.front = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        if self.front == len(self.queue):
            return None
            
        self.front += 1
        return self.queue[self.front-1]
        

    def peek(self) -> int:
        return self.queue[self.front]
        

    def empty(self) -> bool:
        return self.front == len(self.queue)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()