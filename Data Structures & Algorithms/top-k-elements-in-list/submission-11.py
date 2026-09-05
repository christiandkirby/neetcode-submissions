class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get the freqs of unique vals
        n = len(nums)
        buckets = [0] * (n+1)
        freq = collections.Counter(nums)

        # Load the distinct vals into buckets
        for num, count in freq.items():
            if buckets[count] == 0:
                buckets[count] = [num]
            else:
                buckets[count].append(num)

        # Loop through the buckets in reverse order
        ans = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ans.extend(buckets[i])
            
            if len(ans) == k:
                break
        return ans