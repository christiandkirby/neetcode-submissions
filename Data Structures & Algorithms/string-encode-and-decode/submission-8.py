class Solution:

    def encode(self, strs: List[str]) -> str:
        # what happens when a list is empty?
        # what happens when strs contains an empty string?
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "$" + s
        
        print(encoded)
        return encoded
    

    def decode(self, s: str) -> List[str]:
        # what happends when s is an empty string
        # what happens when s is 
        i = 0
        og_str_list = []

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1
            
            length = int(s[i : j])
            
            i = j + 1
            j = i + length

            og_str_list.append(s[i:j])

            i = j
        return og_str_list

