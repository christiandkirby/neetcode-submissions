class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = {}

        for num in nums:
            if num in Map:
                return True
            Map.update({num:0})
        return False
         