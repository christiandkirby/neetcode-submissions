class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: Integer Array(nums), Integer(target)
        # Output: Integer Array

        # Keep track of each val and their index
        tracker = {}

        for k, v in enumerate(nums):
            tracker[v] = k
        
        for i in range(len(nums)):
            if target - nums[i] in tracker and i != tracker.get(target - nums[i]):
                return [i, tracker.get(target - nums[i])]