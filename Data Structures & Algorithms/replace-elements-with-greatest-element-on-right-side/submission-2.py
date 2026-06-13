class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reverse through array keeping track of max value

        rightMax = -1
        res = [0] * len(arr) 
        for i in range(len(arr) - 1, -1 , -1):
            res[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return res


        # [2, 4, 5, 3, 1, 2]
        # []

