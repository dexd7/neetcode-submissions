class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = count.most_common(k)
        ret=[]
        for i in ans:
            ret.append(i[0])
        return ret