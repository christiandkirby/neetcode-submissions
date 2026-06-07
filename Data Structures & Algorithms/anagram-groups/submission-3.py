from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: String Array
        # Output: Array of String Arrays

        # Create dict to track common anagrams words
        anaTracker = defaultdict(list)

        # Goes through strs, sorts letters in alpha order
        # and check if its already in the dict
        # updates accordingly

        for s in strs:
            alpha_s = "".join(sorted(s))
            if alpha_s not in anaTracker:
                anaTracker[alpha_s] = []
            anaTracker[alpha_s].append(s)
        
        res = []
        for key in anaTracker.keys():
            res.append(anaTracker.get(key))
        return res