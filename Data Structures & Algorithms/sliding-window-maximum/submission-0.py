class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1

        ans = []

        while right < len(nums):
            max_num = max(nums[left:right+1])
            ans.append(max_num)
            left += 1
            right += 1
        return ans