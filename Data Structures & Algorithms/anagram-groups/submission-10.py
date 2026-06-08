from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a dictionary where the key is a string 
        # of letter occurences and the values are the words

        # Input: An array of strings
        # Output: list of string list

        # Questions:
        #   - Are the strings case sensitive?
        #   - What is the desired output representation?
        #       - sorted by number of words?

        group_anagrams = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord("a")] += 1
            group_anagrams[tuple(key)].append(s) # Changed to Tuple b/c its immutable and hashable
        return list(group_anagrams.values())
        