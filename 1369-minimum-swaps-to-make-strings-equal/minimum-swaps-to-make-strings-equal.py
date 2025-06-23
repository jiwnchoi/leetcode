from collections import Counter

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt = 0
        last_c1, last_c2 = None, None
        
        x_in_s1 = 0
        y_in_s1 = 0

        for c1, c2 in zip(list(s1), list(s2)):
            if c1 == c2: continue
            
            if c1 == "x":
                x_in_s1 +=1
            else:
                y_in_s1 += 1

        if (x_in_s1 + y_in_s1) % 2 != 0:
            return -1

        return x_in_s1 // 2 + y_in_s1 // 2 + x_in_s1 % 2 + y_in_s1 % 2
                
