class MinStack:

    def __init__(self):
        self.arr = []
        self.pastMinimums = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.pastMinimums:
            self.pastMinimums.append(val)
        else:
            self.pastMinimums.append(min(val, self.pastMinimums[-1]))
        return None

    def pop(self) -> None:
        self.arr.pop()
        self.pastMinimums.pop()
        return None

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.pastMinimums[-1]

        
