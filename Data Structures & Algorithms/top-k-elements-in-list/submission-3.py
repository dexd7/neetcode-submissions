class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        tracker = {}
        for i in range(len(nums) + 1):
            tracker[i] = []
        for num,c in count.items():
            tracker[c].append(num)
        answer = []
        for i in range(len(nums), 0, -1):
            if tracker[i] != []:
                for j in tracker[i]:
                    answer.append(j)
                    if len(answer) == k:
                        return answer
