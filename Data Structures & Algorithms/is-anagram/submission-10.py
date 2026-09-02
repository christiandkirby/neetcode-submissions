class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        s_count = [0] * 26

        for i in range(n):
            s_count[ord(s[i]) - ord("a")] += 1
            s_count[ord(t[i]) - ord("a")] -= 1
        

        for val in s_count:
            if val != 0:
                return False
        return True