class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        need a set or something to hold this don't know why though, just a hunch
        have to go through the array twice for sure to add it twice
        how do I do sets in python again?
        never mind we don't need a set that's for unique vals
        so we need to return an array
        so maybe we don't need any fancy data structures
        '''

        ans = []
        
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        
        
        return ans


