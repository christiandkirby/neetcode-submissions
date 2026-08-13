class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_element = float("inf")

        while l <= r:
            m = (l+r)//2
            if nums[l] < nums[m] and nums[l] < nums[r]:
                r = m - 1
                min_element = min(min_element, nums[l])
            elif nums[r] < nums[m] and nums[r] < nums[l]:
                l = m + 1
                min_element = min(min_element, nums[r])
            else:
                min_element = min(min_element, nums[m])
                l += 1
                r -= 1
        return min_element

