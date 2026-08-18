class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newNums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            if i != 0 and newNums[i] == newNums[i-1]:
                continue
            currSum = newNums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                newSum = currSum+newNums[l]+newNums[r]
                if newSum<0:
                    l+=1
                elif newSum>0:
                    r-=1
                else:
                    ans.append([newNums[i],newNums[l],newNums[r]])
                    l+=1
                    r-=1
                    while l < r and newNums[l] == newNums[l - 1]:
                        l += 1
                    while l < r and newNums[r] == newNums[r + 1]:
                        r -= 1
        return ans
