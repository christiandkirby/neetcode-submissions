from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: String Array
        # Output: Array of String Arrays

        a = defaultdict(list)

        # Bruteforce: 
        # sort all words and use that as the key
        # Problem is sorting is O(n log n) and it would happen n times
        # therefore being O(n^2) overall

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord("a")] += 1
            a[str(key)].append(s)
        return list(a.values())




