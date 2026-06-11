class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ["act","pots","tops","cat","stop","hat"]
        act: [act, cat]
        '''
        d = defaultdict(list)

        for word in strs:
            d[''.join(sorted(word))].append(word)

        finalList = []
        for key in d:
            finalList.append(d[key])
        return finalList

