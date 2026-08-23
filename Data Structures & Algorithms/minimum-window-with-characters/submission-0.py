class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0: return ''
        need = Counter(t)
        missing = len(t)
        l = best_l = 0
        minimum = float('inf')
        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing-=1
            need[ch]-=1
            while missing == 0:
                if r-l+1 < minimum:
                    minimum = r-l+1
                    best_l = l
                need[s[l]]+=1
                if need[s[l]] > 0:
                    missing+=1
                l+=1
        return s[best_l:best_l + minimum] if minimum != float('inf') else ''
                             
            

