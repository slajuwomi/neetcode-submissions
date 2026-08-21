class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        for k in range(len(nums)):
            if nums[k] != val:
                nums[head] = nums[k]
                head += 1
        return head