class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        counter_s2 = Counter(s2[:len(s1)])
        if counter_s1 == counter_s2:
            return True
        for i in range(len(s1), len(s2)):
            counter_s2[s2[i]] += 1
            counter_s2[s2[i-len(s1)]] -=1
            if counter_s2[s2[i-len(s1)]] == 0:
                del counter_s2[s2[i-len(s1)]]
            if counter_s1 == counter_s2:
                return True
        return False
            