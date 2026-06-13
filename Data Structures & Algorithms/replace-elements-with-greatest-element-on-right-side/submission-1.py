class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        for i in range(len(arr)-1):
            rMax = arr[i+1] 
            for j in range(i+1, len(arr)):
                rMax = max(rMax, arr[j]) 
            res[i] = rMax
        res[-1] = -1
        return res