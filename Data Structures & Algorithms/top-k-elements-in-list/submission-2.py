class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)+1):
            tracker[i] = []
        result = Counter(nums)
        for num, count in result.items():
            tracker[count].append(num)
        answer = []
        for j in range(len(tracker)-1,-1,-1):
            for numb in tracker[j]:
                answer.append(numb)
                if len(answer) == k:
                    return answer





        

