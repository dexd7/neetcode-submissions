class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            sorted_map[tuple(count)].append(word)
        return list(sorted_map.values())