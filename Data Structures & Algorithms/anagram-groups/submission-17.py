class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in sortedMap:
                sortedMap[sortedWord].append(word)
            else:
                sortedMap[sortedWord] = [word]
        return list(sortedMap.values())