from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        output = []

        while r < len(nums):
            # Popping Smaller Values From the Queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove Left Value From Window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
