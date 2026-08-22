class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        curr_max = -1
        for i in range(-1, -(len(arr)) - 1, -1):
            res[i] = curr_max
            curr_max = max(arr[i], curr_max)
        return res
            
        #  i
        # [2,4,5,3,1,2]
        # [0,5,3,2,2,-1]
        # cmax = 5