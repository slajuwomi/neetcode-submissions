class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = 0

    def push(self, val: int) -> None:
        self.arr.append(val)
        return None

    def pop(self) -> None:
        self.arr.pop()
        return None

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return min(self.arr) 

        
