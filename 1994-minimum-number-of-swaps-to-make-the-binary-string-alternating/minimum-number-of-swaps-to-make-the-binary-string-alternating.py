from collections import Counter

class Solution:
    def minSwaps(self, s: str) -> int:
        c = Counter(s)

        if abs(c['1'] - c['0']) > 1:
            return -1
        
        if c['1'] > c['0']:
            # 1010101
            cnt = 0
            for i, char in enumerate(list(s)):
                if i % 2 == 1 and char != "0":
                    cnt +=1
            return cnt

        
        if c['1'] == c['0']:
            # 101010
            cnt1 = 0
            for i, char in enumerate(list(s)):
                if i % 2 == 1 and char != "0":
                    cnt1 +=1
            
            cnt2 = 0
            for i, char in enumerate(list(s)):
                if i % 2 == 1 and char != "1":
                    cnt2 +=1
            return min(cnt1, cnt2)
             
        
        if c['1'] < c['0']:
            # 01010
            cnt = 0
            for i, char in enumerate(list(s)):
                if i % 2 == 1 and char != "1":
                    cnt +=1
            return cnt