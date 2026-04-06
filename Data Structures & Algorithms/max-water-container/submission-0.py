class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        area = 0

        while l < r:
            area = max(( min(heights[l], heights[r]) * (r - l)), area)
            print(f"Area: {area}, the Height: {min(heights[l], heights[l])}, Width {(r - l)}")
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                
        return area
