class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float('inf')]      

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = min(self.minimum[-1], val)
        self.minimum.append(temp)

    def pop(self) -> None:
        self.minimum.pop()
        self.stack.pop()
       
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
