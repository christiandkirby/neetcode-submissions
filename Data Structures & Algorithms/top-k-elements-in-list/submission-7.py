class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [0] * (n+1)
        freq = collections.Counter(nums)

        for num, freq in freq.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ans = []
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i]) # Need explanation por qué
            
            if len(ans) == k:
                break
        
        return ans
