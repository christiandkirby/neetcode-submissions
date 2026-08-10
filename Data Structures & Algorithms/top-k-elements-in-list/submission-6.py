import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict  =  collections.Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)
        ans = []
        
        for key, val in count_dict.items():
            if buckets[val] == 0:
                buckets[val] = [key]
            else:
                buckets[val].append(key)
    
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i])
            if len(ans) == k:
                break
        return ans

