from typing import List
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
            anaTracker[alpha_s].append(s)
        
        return list(anaTracker.values())

        # Time Complexity: O(N log N), where N is the num strings in array strs
        # Space Complexity: O(N), where N is the num of strings in strs
