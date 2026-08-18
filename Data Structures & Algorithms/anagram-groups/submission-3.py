class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for string in strs:
            char = [0]*26
            for y in string:
                char[ord(y) - ord('a')] += 1
            group[tuple(char)].append(string)
        return list(group.values()) 