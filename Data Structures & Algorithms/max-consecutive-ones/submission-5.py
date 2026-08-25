class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr_max = 0
        for n in nums:
            if n == 1:
                curr_max += 1
            else:
                curr_max = 0
            res = max(curr_max, res)
        res = max(curr_max, res)
        return res