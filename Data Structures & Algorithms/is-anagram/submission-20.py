class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        trackers = {}
        for c in s:
            if c in trackers:
                trackers[c]+=1
            else:
                trackers[c]=1
        trackert = {}
        for c in t:
            if c not in trackers or trackers[c]==0:
                return False
            if c in trackers and trackers[c]>=0:
                trackers[c]-=1
        return True
        