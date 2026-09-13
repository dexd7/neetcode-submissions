class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        possible_max_heights = []
        maxArea = 0
        for index, height in enumerate(heights):
            valid_starting_point = index
            while possible_max_heights and possible_max_heights[-1][1]>height:
                new_start, old_possible_height = possible_max_heights.pop()
                valid_starting_point  = new_start
                maxArea = max(maxArea, (index-new_start)*old_possible_height)
            possible_max_heights.append([valid_starting_point, height])
        for i, h in possible_max_heights:
            maxArea = max(maxArea, (len(heights)-i)*h)
        return maxArea
