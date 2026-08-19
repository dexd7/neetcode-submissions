class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dictionary = {}
        for num in nums:
            dictionary[num] = 1+dictionary.get(num, 0)
        i = 0
        for bucket in range(3):
            count = dictionary.get(bucket, 0)
            while count>0:
                nums[i] = bucket
                count-=1
                i+=1