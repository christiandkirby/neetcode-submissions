class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize Dictionary
        numdict = {} 
        # Loops through nums and populates dictionary
        for i , n in enumerate(nums):
            diff = target - n
            if diff in numdict:
                return [numdict[diff], i]
            numdict[n] = i

        