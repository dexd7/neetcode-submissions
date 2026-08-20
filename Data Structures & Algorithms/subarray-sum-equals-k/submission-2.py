class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #empty prefix sum occurs once:
        prefixSum = {0: 1}
        curSum = 0
        subArrays = 0
        for num in nums:
            curSum += num
            diff = curSum-k
            subArrays += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return subArrays
        