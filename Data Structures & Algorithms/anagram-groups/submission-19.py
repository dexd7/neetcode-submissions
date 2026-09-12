class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for word in strs:
            char_array = [0] * 26
            for ch in word:
                char_array[ord(ch)-ord('a')] += 1
            groupings[tuple(char_array)].append(word)
        return list(groupings.values())