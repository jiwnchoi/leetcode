class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        start, end= 1, 2 ** (n-1)
        mid = (start + end) // 2
        current = False
        
        for _ in range(n):
            if k > mid:
                current = not current
                start = mid + 1
                mid = (start + end) // 2
            else:
                end = mid
                mid = (start+end) // 2

        return int(current)