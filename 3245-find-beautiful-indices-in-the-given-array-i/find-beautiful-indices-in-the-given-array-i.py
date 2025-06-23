from bisect import bisect_left
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_candi = []
        for i in range(len(s) - len(a)+1):
            if s[i:i+len(a)] == a:
                a_candi.append(i)

        b_candi = []
        for i in range(len(s) - len(b)+1):
            if s[i:i+len(b)] == b:
                b_candi.append(i)

        result = []
        
        if len(a_candi) == 0 or len(b_candi) == 0:
            return []

        for i in a_candi:
            x = bisect_left(b_candi, i)
            if x > 0 and abs(b_candi[x-1] - i) <= k:
                result.append(i)
            
            elif x <= len(b_candi) -1 and abs(b_candi[x] - i) <= k:
                result.append(i)

        return result
        