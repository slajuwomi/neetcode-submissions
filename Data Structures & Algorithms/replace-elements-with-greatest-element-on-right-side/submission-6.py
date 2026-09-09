class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # done by going right to left and keeping the max as you go along
        res = [0] * len(arr)
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            res[i] = cur_max
            cur_max = max(arr[i], cur_max)
        return res 