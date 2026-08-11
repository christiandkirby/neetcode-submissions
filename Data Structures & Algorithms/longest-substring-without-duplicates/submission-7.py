class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        longest = 0

        for r in range(len(s)):
            curr_char = s[r]
            while curr_char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(curr_char)
            longest = max(longest, (r - l + 1))
        return longest
