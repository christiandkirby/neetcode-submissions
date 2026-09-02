class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}

        for idx, val in enumerate(nums):
            nums_idx[val] = idx
        
        for i in range(len(nums)):
            need = target - nums[i]
            num = nums[i]
            j = nums_idx.get(need)

            if need in nums_idx and i != j:
                return [i, j] if i < j else [j, i]

            