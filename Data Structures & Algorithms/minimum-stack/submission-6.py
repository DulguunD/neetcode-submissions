class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []      
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_min = min(self.current_min, val)
        self.minimum.append((val, self.current_min))
        # print(f"Inserted: {val}, stack: {self.stack}, dict: {self.minimum}")

        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        if self.minimum:
            self.current_min = self.minimum[-1][1]
        else:
            self.current_min = float('inf')
        # print(f"Popped: {self.stack}, mini: {self.minimum}, currrent_min: {self.current_min}")

        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        # print(f"GetMin: {self.stack}, dict: {self.minimum}")
        return self.minimum[-1][1]
