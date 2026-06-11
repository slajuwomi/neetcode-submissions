class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        biggestSoFar = 0
        consecutiveOnes = 0
        # brute force
        for n in nums:
            if n == 1:
                consecutiveOnes += 1
            else:
                biggestSoFar = max(consecutiveOnes, biggestSoFar)
                consecutiveOnes = 0
        biggestSoFar = max(consecutiveOnes, biggestSoFar)
        return biggestSoFar
        