import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = [
            -n for n in nums
        ]
        heapq.heapify(heap)
        for _ in range(k):
            v = - heapq.heappop(heap)
            ans += v
            heapq.heappush(heap, -ceil(v / 3))

        return ans



