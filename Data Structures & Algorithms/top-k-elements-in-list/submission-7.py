class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order = defaultdict(list)
        count = Counter(nums)
        for nu,co in count.items():
            order[co].append(nu)
        ans = []
        for i in range(len(nums),-1,-1):
            if order[i]:
                for j in order[i]:
                    ans.append(j)
                    if len(ans) == k:
                        return ans

            