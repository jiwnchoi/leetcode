from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)

        heap = []


        for word, n in dict(c).items():
            heapq.heappush(heap, (-n, word))

        return [
            heapq.heappop(heap)[1]
            for _ in range(k)
        ]
