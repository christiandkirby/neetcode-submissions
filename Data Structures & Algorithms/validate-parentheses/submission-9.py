class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False
        
        braces_dict = {"}":"{", 
                        "]":"[", 
                        ")":"("}

        stack = []

        for b in s:
            if b not in braces_dict:
                stack.append(b)
            else:
                if not stack:
                    return False
                else: 
                    if braces_dict.get(b) != stack[-1]:
                        return False
                    else:
                        stack.pop()
        return True if not stack else False