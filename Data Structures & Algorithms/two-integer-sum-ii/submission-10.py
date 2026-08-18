class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while r<len(numbers):
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total!=target and r == len(numbers) - 1:
                l+=1
                r = l+1
                continue
            else:
                r+=1   
         
            
