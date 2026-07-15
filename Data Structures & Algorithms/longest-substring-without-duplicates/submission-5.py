class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        ans = 0
        chars = set()

        if len(s) < 2:
            return len(s)

        while j < len(s):
            curr_char = s[j]
            if curr_char in chars:
                chars.remove(s[i])
                i += 1
            else:
                chars.add(curr_char)
                ans = max(ans, j-i+1)
                j += 1
        return ans
