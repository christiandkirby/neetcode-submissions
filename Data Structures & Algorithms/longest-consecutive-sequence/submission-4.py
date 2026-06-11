class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: Int Array
        # Output: Int (len of longest consec Seq)

        # Don't forget edge cases for arrays of length <= 1
        if len(nums) <= 1:
            return len(nums)
        
        num_set = set(nums) # O(N) Space
        longest = 1
        
        for i in range(len(nums)): # O(N) Time
            start = nums[i]
            if start - 1 not in num_set:
                k = 1
                while start + k in num_set:
                    k += 1
                longest = max(longest, k)
            else:
                continue
        return longest
    
        # Time Complexity : O(N)
        # Space Complexity : O(N)

        