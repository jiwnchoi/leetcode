from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        
        i = idx - 1
        j = idx
        
        while j - i - 1 < k:
            if i < 0:
                j += 1
            elif j >= len(arr):
                i -= 1
            elif abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
                
        return arr[i+1:j]