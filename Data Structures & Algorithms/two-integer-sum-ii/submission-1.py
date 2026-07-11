class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        idx1, idx2 = 0, n-1

        while idx1 < idx2:
            curr_sum = numbers[idx1] + numbers[idx2]
            if curr_sum == target:
                return [idx1+1, idx2+1]
            
            if curr_sum < target:
                idx1 += 1
            else:
                idx2 -= 1