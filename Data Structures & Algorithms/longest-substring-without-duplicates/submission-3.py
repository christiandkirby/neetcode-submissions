class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Input: String
        # Output: Integer

        # Sliding Window Question
        # Valid Substring: Substring has all unique letters
        # while phrase should be while the substring is invalid

        l = 0
        longest = 0
        s_set = set()
        
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            longest = max(longest, r-l+1)
        return longest