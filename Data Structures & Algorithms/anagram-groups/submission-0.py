class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ayusman = defaultdict(list) #[] -> []
        
        for i in strs:
            count = [0]*26
            for y in i:
                count[ord(y) - ord('a')] += 1
            ayusman[tuple(count)].append(i)
        return list(ayusman.values())
            