class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            # Handles Edge Case if length > 9
            while s[j]!= "#":
                j += 1
            
            length = int(s[i : j])
            i = j + 1
            j = i + length

            ans.append(s[i:j])

            i = j # Goes to the next length string
        return ans
