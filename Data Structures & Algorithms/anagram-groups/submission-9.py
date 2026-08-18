class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            count = [0]*26
            for i in word:
                count[ord('a')-ord(i)] +=1
            group[tuple(count)].append(word)
        return list(group.values())


        