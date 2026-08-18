class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_map = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            for letter in strs[i]:
                count[ord(letter)-ord('a')]+=1
            frequency_map[tuple(count)].append(strs[i])
        res = []
        for value in frequency_map.values():
            res.append(value)
        return res