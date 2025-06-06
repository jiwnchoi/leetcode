class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = set(range(1, n+1))        
        added = 1
        a = 1

        for a in range(1, n+1):
            if a > k // 2:
                continue
            
            if k-a in arr and k-a != a:
                arr.remove(k-a)
                while k - (n+added) in arr:
                    added +=1
                arr.add(n + added)
                added +=1
            a += 1
        return sum(arr)

                        