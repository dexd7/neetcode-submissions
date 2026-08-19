class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        contender = 0
        count = 0
        for i in nums:
            if count == 0:
                contender = i
                count +=1
            else:
                count += 1 if contender == i else -1
        return contender