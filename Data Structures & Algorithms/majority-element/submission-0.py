class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set()
        limit = len(nums) // 2
        for num in nums:
            s.add(num)
        for num in s:
            if nums.count(num) > limit:
                return num