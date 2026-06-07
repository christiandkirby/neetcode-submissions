class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input: 2 Strings s and t
        # Output: Boolean (T or F)

        # Goal: Return True if strings s and t are anagrams of each 
        # other, otherwise return False

        # Questions:
        # 1) Is sorting allowed?
        # 2) Is the input case sensitive?
        #   - All lowercase?


        # Base Cases:
        if len(s) != len(t):
            return False

        
        # If sorting is allowed:
        # return sorted(s) == sorted(t)

        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # If sorting isn't allowed

        anagram_arr = [0]*26


        for c in s:
            anagram_arr[ord(c) - ord('a')] += 1
        for c in t:
            anagram_arr[ord(c) - ord('a')] -= 1
        
        for a in anagram_arr:
            if a != 0:
                return False
        return True


        # Time Complexity : O(N + M) (can be reduced to O(N) since N = M)
        # Space Complexity: O(1) (26 is a constant value)


