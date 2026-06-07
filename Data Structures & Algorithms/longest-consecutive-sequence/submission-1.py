class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove the duplicates
        # ***Constant Search Time***
        numSet = set(nums)

        # Ouput must be max sequence number
        # Res gets updated if a new found seqence is found
        res = 0
        
        # Loop through the set
        # Check if nums[i] - 1 exists in the set
        # if not, that number starts a sequence
        # If it does, keep checking if nums[i] + 1 exists
        
        for num in nums:
            if(num - 1) not in numSet: # Checks if num - 1 isnt in the Set
                length = 0
                # adds length to num to keep up with sequence existence
                while (num + length) in numSet:
                    length += 1
                res = max(length, res) # Adjust Max Sequence Length
        return res



