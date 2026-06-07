class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        c_set = set()
        
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            c_set.add(s[r])
            longest = max(longest, (r-l+1))
        return longest