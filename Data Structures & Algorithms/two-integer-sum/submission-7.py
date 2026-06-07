class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Is nums sorted in ascending order?
        # If so, then a Two Pointer Approach

        # If not, then use a hashmap
        numDict = {}
        ans = [0,1]

        # Load the vals and their indices into the dictionary
        for v, k in enumerate(nums):
            numDict[k] = v

        for i in range(len(nums)):
            if target - nums[i] in numDict and i != numDict.get(target - nums[i]):
                return [i, numDict.get(target - nums[i])]