class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0
        
        while l < r:
            #               |
            # | -  -  -  -  | 
            # |    water    |
            # ---------------
            # 7             8 
            # L             R
            # Height - Water can only rise to the shorter wall.
            # Width - This is the distance between the two walls.
            # area = height * width
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
                
        return result