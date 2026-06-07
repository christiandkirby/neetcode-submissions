class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Load a dictionary with all the freq from the list
        # loop over the the dictionary and using k as the range
        # append the max freq to res array until you reach k
        # return res

        # *** BUCKET SORT ALGORITHM ***

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            # Updates dictionary, and defaults val to 0 if not already in dict
            count[num] = 1 + count.get(num, 0)
              
        
        for num, c in count.items():
            freq[c].append(num)
        
        # starts at len(freq) - 1, loops until i=0, decrements by one
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:#looping through sub-array in freq[i]
                res.append(n)
                if len(res) == k: #checks if len(res) == k, and returns if True
                    return res
        
        