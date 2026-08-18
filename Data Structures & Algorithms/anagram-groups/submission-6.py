class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for i in strs:
            counter = [0]*26
            for y in i:    
                counter[ord('a')-ord(y)] += 1
            table[tuple(counter)].append(i)
        return list(table.values())
            