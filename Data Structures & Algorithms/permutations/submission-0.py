class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        if nums == []:
            return res
        def permut():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for n in nums:
                if n in subset:
                    continue
                subset.append(n)
                permut()
                subset.pop()
        permut()
        return res