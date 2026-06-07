class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Encodes word with (word length) + "*" delimeter,
            # and then the word
           encoded += str(len(s)) + "*" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j]) #Grabs the length, makes it an int
            res.append(s[j + 1: j + 1 + length]) # appends decoded word to result array
            i = j + 1 + length # Updates index to start of nextdecode sequence
        return res
