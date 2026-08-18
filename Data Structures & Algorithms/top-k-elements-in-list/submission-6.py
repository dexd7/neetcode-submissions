class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = defaultdict(list)

        result = Counter(nums) 
        for num, count in result.items():
            track[count].append(num)
        answer = []
        lent = max(result.values())
        for y in range(lent, 0, -1):
            for n in track[y]:
                answer.append(n)
                if len(answer) == k:
                    return answer