class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): #This is a base case
            return False
        
        l = 0
        s1_array = [0] * 26
        s2_array = [0] * 26

        for c in s1:
            s1_array[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            if (r-l+1) < len(s1):
                s2_array[ord(s2[r]) - ord('a')] += 1
                continue
            
            s2_array[ord(s2[r]) - ord('a')] += 1
            if s2_array == s1_array:
                return True
            else:
                s2_array[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False


