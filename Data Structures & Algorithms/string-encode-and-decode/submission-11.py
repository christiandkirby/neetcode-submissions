class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "%" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:

        i, j = 0, 0
        ans = []

        while i < len(s) and j < len(s):

            while s[j] != "%":
                j += 1
            
            num_len = int(s[i:j])

            i = j + 1
            j = i + num_len

            ans.append(s[i:j])
            
            i = j
        return ans



