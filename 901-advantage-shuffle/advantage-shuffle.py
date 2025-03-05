from bisect import bisect_left

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        shuffled = [-1 for _ in range(len(nums2))]
        used = [False for _ in sorted_nums1]
        
        for j, num in enumerate(nums2):
            i = bisect_left(sorted_nums1, num+1)
            if i == len(sorted_nums1):
                continue
            
            while i < len(used) and used[i] == True:
                i += 1

            if i == len(used):
                continue
            
            shuffled[j] = sorted_nums1[i]
            used[i] = True
        
        remains = [sorted_nums1[i] for i in range(len(used)) if used[i] == False]

        for i, num in enumerate(shuffled):
            if num != -1:
                continue

            shuffled[i] = remains.pop()
        return shuffled