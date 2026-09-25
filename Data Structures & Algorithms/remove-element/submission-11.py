class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = end = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[end], nums[i] = nums[i], nums[end]
                k += 1
                end += 1
        print(nums)
        return k
            
            
