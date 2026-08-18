class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l<r:
            if numbers[l] + numbers[r] != target:
                if r == len(numbers)-1:
                    l+=1
                    r = l+1
                    continue
                else:
                    r+=1
            else:
                return [l+1,r+1]