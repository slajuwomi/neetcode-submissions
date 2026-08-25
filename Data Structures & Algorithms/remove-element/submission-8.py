class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        for k in range(len(nums)):
            if nums[k] != val:
                nums[first] = nums[k]
                first +=1
        return first