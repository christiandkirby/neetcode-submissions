class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        n = len(heights)
        L, R = 0, n-1

        while L < R:
            curr_container = min(heights[L], heights[R]) * (R - L)
            max_container = max(max_container, curr_container)
            
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_container
