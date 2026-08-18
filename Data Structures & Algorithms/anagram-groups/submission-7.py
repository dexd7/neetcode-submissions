class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
       
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord('a')-ord(char)] +=1
            group[tuple(count)].append(string)
        return list(group.values())
                 