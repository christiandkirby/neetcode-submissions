from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the frequencies of the numbers
        # Put the numbers in a dictionary as a list 
        # Loop through the key with the highest freqency
        
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                # Apparently allowed since we can guarentee the answer is unique.
                # Also, you can fully grab the inner array because of this 
                # assumption as well.
                ret.extend(buckets[i]) #[1,2,3] extend([4,5]) --> [1,2,3,4,5]
            if len(ret) == k:
                break
        return ret
       