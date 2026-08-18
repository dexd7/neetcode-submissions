class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}

        for i in range(len(nums)+1):
            track[i] = []
        result = Counter(nums) 
        for num, count in result.items():
            track[count].append(num)
        answer = []
        for y in range(len(track)-1, -1, -1):
            for n in track[y]:
                answer.append(n)
                if len(answer) == k:
                    return answer



        

