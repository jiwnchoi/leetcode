class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        character1 = list(word1)
        character2 = list(word2)

        for i in range(max(len(character1), len(character2))):
            if i < len(character1):
                output += character1[i]
            if i < len(character2):
                output += character2[i]

        return output