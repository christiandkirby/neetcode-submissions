class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input: String
        # Output: Boolean Val

        # Make sure string is all lowercase

        # Loop through the string
        # Check if a val is alphanumeric

        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True

       