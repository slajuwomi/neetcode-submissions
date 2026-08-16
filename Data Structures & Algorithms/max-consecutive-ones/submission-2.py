class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                res = max(current, res)
                current = 0
        res = max(current, res)
        return res