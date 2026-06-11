class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_map = {}
        #   i = index, n = value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in checked_map:
                return [checked_map[diff], i]
            checked_map[n] = i
        return