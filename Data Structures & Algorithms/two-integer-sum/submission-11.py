class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # What is the data representation
        #   - Is it sorted or not?
        # If not sorted is sorting allowed?

        i = 0
        my_dict = {val : key for key, val in enumerate(nums)}


        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                if i != my_dict.get(diff):
                    if i < my_dict.get(diff):
                        return [i, my_dict.get(diff)]
                    else:
                        return [my_dict.get(diff), i]
        
        # Time Complexity : O(N)
        # Space Complexity : O(N)