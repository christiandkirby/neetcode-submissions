class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # Didn't think about sorting
        sum_set = []
        n = len(nums)

        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0 and i != j and j != k and i != k:
                    if [nums[i], nums[j], nums[k]] not in sum_set:
                        sum_set.append([nums[i], nums[j], nums[k]])

                if curr_sum < 0:
                    j += 1
                else:
                    k -= 1
        return sum_set