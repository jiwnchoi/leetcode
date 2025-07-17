class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash_map = {}
        answer = -1

        for i, card in enumerate(cards):
            if card in hash_map:
                dist = i - hash_map[card] + 1
                answer = min(answer, dist) if answer != -1 else dist
            hash_map[card] = i

        return answer 
