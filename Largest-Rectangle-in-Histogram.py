class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        n = len(heights)
        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                width = i-index
                maxArea = max(width*height,maxArea)
                start = index
            stack.append((start,heights[i]))

        while stack:
            index, height = stack.pop()
            width = n-index
            maxArea = max(maxArea, width*height)
        return maxArea
        
       
        