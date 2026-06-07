class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Maps charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                # Uses ord() which grabs the ASCII value for a character
                # Updates count but using ASCII num difference to index array
                # Adds 1 to the value at the index
                count[ord(c) - ord("a")] += 1 
                # Must use a tuple since in python, mutable iterables can't be keys
            res[tuple(count)].append(s)
        return res.values()


        
        