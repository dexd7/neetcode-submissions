class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights)-1
        l = 0
        max_a = 0
        while l<r:
            if heights[l] < heights[r]:
                side = heights[l]
                l+=1
            else:
                side = heights[r]
                r-=1
            area = side*(r-l+1)
            max_a = max(max_a,area)
        return max_a
        