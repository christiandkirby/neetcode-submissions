from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)

        for word in strs:
            word_key = [0] * 26
            for c in word:
                word_key[ord(c) - ord("a")] += 1
            
            word_key = tuple(word_key)
            
            if word_key not in anagram_dict:
                anagram_dict.get(word_key,[])
                anagram_dict[word_key].append(word)
            else:
                anagram_dict[word_key].append(word)
        return list(anagram_dict.values())
