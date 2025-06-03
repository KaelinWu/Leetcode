class Solution:
    def trap(self, height: List[int]) -> int:
        
        area = 0
        l = 0
        r = len(height)-1
        max_left = height[0]
        max_right = height[-1]
        while l < r:
            if max_left < max_right:
                l+=1
                max_left = max(max_left, height[l])
                area += max_left-height[l]
            else:
                r-=1
                max_right = max(max_right, height[r])
                area += max_right-height[r]
        return area
        
       





        