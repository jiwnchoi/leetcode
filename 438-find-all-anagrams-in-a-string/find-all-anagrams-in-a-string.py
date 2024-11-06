from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(list(p))
        def is_anagram(chunk: str):
            count_chunk = Counter(list(chunk))
            for char, val in count_chunk.items():
                if count_p[char] != val:
                    return False
            return True

        return [
            i
            for i in range(0, len(s) - len(p)+1)
            if is_anagram(s[i:i+len(p)])
        ]
            