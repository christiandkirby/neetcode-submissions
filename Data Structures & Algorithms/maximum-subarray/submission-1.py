class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        i = 0

        while i < len(nums):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
            i += 1
        return maxSum