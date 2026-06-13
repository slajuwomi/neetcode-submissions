class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0 
        freeSpotIndex = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[freeSpotIndex] = nums[index]
                freeSpotIndex += 1
                res += 1
        print(res)
        return res 
        