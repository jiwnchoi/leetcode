class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        c = set([s[0]])

        i = 0
        j = 1

        max_len = 1

        while i < len(s) and j < len(s):
            if s[j] in c:
                c.remove(s[i])
                i += 1

            elif s[j] not in c:
                c.add(s[j])
                j +=1
            if max_len < j - i:
                max_len = j-i
            
            
        return max_len
            


            

            
