class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        prevOps = []

        for i in range(len(operations)):
            curOp = operations[i]
            if curOp == "D":
                prevOps.append(prevOps[-1]*2)
            elif curOp == "C":
                prevOps.pop()
            elif curOp == "+":
                prevOps.append(prevOps[-1] + prevOps[-2])
            else:
                prevOps.append(int(curOp))

        return sum(prevOps) 


                
        