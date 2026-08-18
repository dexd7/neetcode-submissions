from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            tracker[tuple(count)].append(word)
        return list(tracker.values())