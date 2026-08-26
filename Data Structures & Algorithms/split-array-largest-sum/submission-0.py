class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #minimum sum of the split would be at least max(nums)
        #maximum sum of the split could be the entire array so sum(nums)
        def canSplit(largest):
            subArrays = 1
            currSum = 0
            for num in nums:
                currSum+=num
                if currSum>largest:
                    subArrays+=1
                    if subArrays>k:
                        return False
                    currSum = num
            return True
                    
        l, r = max(nums), sum(nums)
        res = 0
        while l<=r:
            mid = l+(r-l)//2
            if canSplit(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
