class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictionary = {}
        for num in nums:
            dictionary[num] = 1+dictionary.get(num, 0)
        result = set()
        majority_qualifier = (len(nums)//3)+1
        for i in nums:
            if dictionary[i]>=majority_qualifier:
                result.add(i)
        return list(result)