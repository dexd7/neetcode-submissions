class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        temp = defaultdict(list)
        ret = []
        for num,count in count.items():
            temp[count].append(num)
        for i in range(len(nums),-1,-1):
            if temp[i]:
                for j in temp[i]:
                    ret.append(j)
                    if len(ret)==k:
                        return ret