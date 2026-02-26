class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        current_height = 0
        le = 0
        n = len(height)
        ri = n-1

        while le < ri:
            if height[le] < height[ri]:
                current_height = min(height[le], height[ri])
                width = ri - le
                max_area = max(max_area, (current_height*width))
                le += 1
            else:
                current_height = min(height[le], height[ri])
                width = ri - le
                max_area = max(max_area, (current_height*width))
                ri -= 1

        return max_area