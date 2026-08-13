class Solution:
    def isValid(self, s: str) -> bool:
        groupings = {"}":"{", 
                     ")":"(",
                     "]":"["}
        stack = []

        for c in s:
            if c not in groupings:
                stack.append(c)
            else:
                if stack:
                    if groupings.get(c) != stack[-1]: # Fails Condition 2
                        return False
                    else: # Handles Condition 1
                        stack.pop()
                else: # Fails Condition 3
                    return False
        return True if not stack else False