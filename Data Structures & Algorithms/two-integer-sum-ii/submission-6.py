class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = 2
        while l<r:
            if numbers[l-1]+numbers[r-1] != target:
                if r==len(numbers):
                    l+=1
                    r = l+1
                    if numbers[l-1] + numbers[r-1] == target:
                        return [l,r] 
                else:
                    r+=1
            else:
                break
        return [l,r]