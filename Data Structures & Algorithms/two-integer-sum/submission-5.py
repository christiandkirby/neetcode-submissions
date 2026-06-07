class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: Integer Array, Integer
        # Output: Integer Array

        # Creates dict for ints and their idices
        myDict = {}
        
        # Loads dict with said int's and indices
        for k, v in enumerate(nums):
            myDict[v] = k
        
        # Loops through arr, checks if target - num is
        # in the array and if the indices are different, 
        # then returns the respective indices 
        for i in range(len(nums)):
            if target - nums[i] in myDict and i != myDict.get(target - nums[i]):
                return [i, myDict.get(target - nums[i])]
        
        # Time Complexity: O(N), where N is number of vals in array
        # Space Complexity: 0(N), where N is number of vals in array

