class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Input: Integer Array
        # Output: Boolean Val

        # Is the data sorted? No

        myDict = {}
        for num in nums:
            if num not in myDict.keys():
                myDict[num] = 0
            else:
                return True
        return False

        