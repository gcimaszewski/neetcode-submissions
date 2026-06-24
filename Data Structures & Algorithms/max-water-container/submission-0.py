class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        def _volume_of_container(h1, h2, i1, i2):
            top = min(h1, h2)
            return (i2 - i1) * top
        
        max_water_volume = 0

        while left < right:
            h_left = heights[left]
            h_right = heights[right]
            volume = _volume_of_container(h_left, h_right, left, right)
            max_water_volume = max(max_water_volume, volume)
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return max_water_volume
        