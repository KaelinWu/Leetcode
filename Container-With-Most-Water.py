class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0
        while l < r:
            h1 = height[l]
            h2 = height[r]
            width = r-l
            area = width * min(h1,h2)
            max_area = max(area,max_area)
            if h1 < h2:
                l+=1
            else:
                r-=1
        return max_area
       
            
