class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l<r:
                sum3 = num+nums[l]+nums[r]
                if sum3 == 0:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif sum3>0:
                    r-=1
                elif sum3<0:
                    l+=1
        return res

        

