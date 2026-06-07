class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_track = defaultdict(int)

        for k,v in enumerate(nums):
            idx_track[v] = k
        
        for i in range(len(nums)):
            if target - nums[i] in idx_track and i != idx_track.get(target - nums[i]):
                return [i, idx_track.get(target - nums[i])]