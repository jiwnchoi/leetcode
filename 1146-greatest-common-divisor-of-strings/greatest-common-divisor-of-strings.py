class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = str1 if len(str1) < len(str2) else str2
        max_str = str1 if len(str1) >= len(str2) else str2
        
        gcds = [""]

        for i in range(1, len(min_str)+1):
            if len(max_str) % i == 0 and \
                len(min_str) % i == 0 and \
                max_str == (min_str[0:i] * (len(max_str) // i)) and \
                min_str == (min_str[0:i] * (len(min_str) // i)):
                
                gcds.append(min_str[0:i])
        return max(gcds, key=lambda x:len(x))

