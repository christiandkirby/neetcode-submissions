class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Question: What is the data representation?
        #   - Is it sorted? 
        # Set : Keep track of all distinct elements
        # Do a linear scan of add into the set
        # Checking if an item has been added or not

        # Goal: Return True if the array conatains duplicates
        # and False otherwise

        distinctElements = set()
        for num in nums:
            if num not in distinctElements:
                distinctElements.add(num)
            else:
                return True
        return False


        # Time Complexity: O(N)
        # Space: 0(N)
