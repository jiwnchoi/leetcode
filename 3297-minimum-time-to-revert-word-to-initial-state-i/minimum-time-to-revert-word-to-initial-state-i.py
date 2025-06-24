class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        for i in range(k, len(word), k):
            if word[i:] == word[0:len(word)-i]:
                return i // k
        
        return ceil(len(word) / k)