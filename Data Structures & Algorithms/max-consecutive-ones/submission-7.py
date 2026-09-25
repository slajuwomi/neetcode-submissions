class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for num in nums:
            if num == 1:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 0
        res = max(cnt, res)
        return res
            
            # cnt += 1 if num == 1 else cnt = 0
        