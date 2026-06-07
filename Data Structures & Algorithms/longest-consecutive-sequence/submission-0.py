class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove the duplicates
        # Constant Search Time
        numSet = set(nums)

        # Ouput must be max sequence number
        # Res gets updated if a new found seqence is found
        res = 0
        
        # Loop through the set
        # Check if nums[i] - 1 exists in the set
        # if not, that number starts a sequence
        # If it does, keep checking if nums[i] + 1 exists
        for num in nums:
            if(num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                res = max(length, res)
        return res



