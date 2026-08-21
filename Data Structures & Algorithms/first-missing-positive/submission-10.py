class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # #Brute Force solution:
        # #Time Complexity: O(n^2)
        # for i in range(1, len(nums)+2):
        #     if i not in nums:
        #         return i
        
        # # Second attempt at slightly optimal approach
        # tracker = [False] * len(nums)
        # for num in nums:
        #     if num>0 and num<=len(nums):
        #         tracker[num-1] = True
        # for i in range(1, len(nums)+1):
        #     if not tracker[i-1]:
        #         return i
        # return len(nums)+1
        # Time Complexity and Space Complexity both become O(n)

        # Third attempt for even better
        
        n = len(nums)
        for i in range(n):
            nums[i] = 0 if nums[i]<0 else nums[i]
        for i in range(n):
            val = abs(nums[i])
            if 1<=val<n+1:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -(n+1)
        for i in range(1,n+1):
            if nums[i-1]>=0:
                return i
        return n+1



        