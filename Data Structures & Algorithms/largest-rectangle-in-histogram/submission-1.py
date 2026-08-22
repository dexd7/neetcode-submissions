class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for ind,height in enumerate(heights):
            start = ind
            while stack and stack[-1][1]>height:
                i,h = stack.pop()
                maxArea = max(maxArea, (ind-i) * h)
                start = i
            stack.append((start, height))
        for i,h in stack:
            maxArea = max(maxArea, (len(heights)-i)*h)
        return maxArea
            