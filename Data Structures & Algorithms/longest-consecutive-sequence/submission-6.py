class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(n) space

        longest = 0
        for num in num_set:
            curr = num
            curr_longest = 0

            while curr in num_set:
                curr_longest += 1
                curr += 1
            
            longest = max(longest, curr_longest)
        return longest

        