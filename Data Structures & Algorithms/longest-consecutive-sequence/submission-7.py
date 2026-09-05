class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_seq = 0

        for num in nums:
            cur_max_seq = 0
            cur_num = num
            if (num-1) in numSet:
                continue
            else:
                while cur_num in numSet:
                    cur_max_seq += 1
                    cur_num += 1
                max_seq = max(max_seq, cur_max_seq)
        
        return max_seq