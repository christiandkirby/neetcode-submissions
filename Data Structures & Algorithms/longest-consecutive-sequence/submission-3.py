class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: Int Array
        # Output: Int (len of longest consec Seq)

        if len(nums) <= 1:
            return len(nums)
        
        num_set = set(nums)
        longest = 1
        
        for i in range(len(nums)):
            start = nums[i]
            if start - 1 not in num_set:
                k = 1
                curr_max = 1
                while start + k in num_set:
                    curr_max += 1
                    k += 1
                longest = max(longest, curr_max)
            else:
                continue
        return longest

        