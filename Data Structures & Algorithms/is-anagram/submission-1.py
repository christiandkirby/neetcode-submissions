class Solution:

    # Time Complexity O(N log N)
    # The use of the sorted func N times AKA Twice
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        