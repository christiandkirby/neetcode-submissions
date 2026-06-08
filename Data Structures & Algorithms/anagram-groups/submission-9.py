from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Make a dictionary where the key is a string 
        # of letter occurences and the values are the words

        # Input: An array of strings
        # Output: list of string list

        group_anagrams = defaultdict(list)

        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord("a")] += 1
            group_anagrams[str(key)].append(s)
        return list(group_anagrams.values())
        