class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        need a stack, pretty much add everything and remove everything from said stack
        """

        stack = []

        for i, op in enumerate(operations):
            print(i)
            if op == "+":
                stack.append(int(stack[-1]+stack[-2]))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1]*2))
            else:
                stack.append(int(op))
        print(stack)
        return sum(stack)