class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Input: String
        # Output: Integer

        l = 0
        longest = 0
        letters = set()
        n = len(s)

        # Loop through string, use a set to keep track of duplicates
        # Use a while loop to check condition i < len(s)
        for r in range(n):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            

            letters.add(s[r])
            w = (r - l) + 1
            longest = max(longest, w)
        
        return longest

        # Time Complexity: O(N)
        # Space Complexity: O(N)