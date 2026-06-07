class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We want to maximize the distance between bar l and r
        # We want the smaller of the bars x the distance = max amount of water

        # Initialize the l and r pointers
        l, r = 0, len(heights) - 1
        
        # Initialze max water value
        maxNum = 0

        # Ensure l > r never happens
        while l < r:
            distance = r - l
            waterNum = min(heights[l],heights[r]) * distance

            maxNum = max(maxNum, waterNum)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxNum



        