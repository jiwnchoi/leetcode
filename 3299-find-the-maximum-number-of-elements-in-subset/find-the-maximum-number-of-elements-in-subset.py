class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        result = 0
        def recurr(num, length):
            if num == 1 and cnt[num] % 2 == 0:
                return cnt[1] - 1
            if num == 1 and cnt[num] % 2 == 1:
                return cnt[1]                
            if cnt[num] >= 2:
                return recurr(num * num, length + 2)
            if cnt[num] == 1:
                return length + 1
            if cnt[num] == 0:
                return length - 1
        
        for key in keys:
            result = max(result, recurr(key, 0))
        
        return result 
            

            
        
            
            

            