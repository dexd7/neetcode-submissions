class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for ind, num in enumerate(nums):
            if ind>0:
                if nums[ind] == nums[ind-1]:
                    continue
            l = ind+1
            r = len(nums)-1
            while l<r:
                zero_req = num + nums[l] + nums[r]
                if zero_req == 0:
                    answers.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif zero_req > 0:
                    r -= 1
                elif zero_req < 0:
                    l += 1
        return answers