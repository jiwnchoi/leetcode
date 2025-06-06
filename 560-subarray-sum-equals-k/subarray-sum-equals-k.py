class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {}
        ans = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            if s == k:
                ans += 1
            if s - k in hm:
                ans += hm[s-k]
            hm[s] = 1 if s not in hm else hm[s] + 1
        print(hm)
        return ans



        
