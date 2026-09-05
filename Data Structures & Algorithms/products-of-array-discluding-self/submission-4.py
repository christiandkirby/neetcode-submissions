class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_mult = 1
        r_mult = 1
        
        l_arr = [0] * n
        r_arr = [0] * n

        for l in range(n):
            l_arr[l] = l_mult
            l_mult *= nums[l]
        
        for r in range(n-1, -1, -1):
            r_arr[r] = r_mult
            r_mult *= nums[r]

        return [l*r for l, r in zip(l_arr, r_arr)]