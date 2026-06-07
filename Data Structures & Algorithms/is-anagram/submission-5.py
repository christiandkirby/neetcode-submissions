class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input: 2 Strings
        # Output: Boolean Val

        # An anagram has the same num or chars
        if len(s) != len(t):
            return False

        # Anagrams have the same quantity for each letter
        s_Dict = Counter(s)
        t_Dict = Counter(t)

        return s_Dict == t_Dict