class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        def get_grad(p1: list[int], p2: list[int]):
            return (p2[1] - p1[1]), (p2[0]-p1[0])

        def compare_grad(g1, g2):
            if not g1 or not g2:
                return False
            return g1[0]*g2[1] == g2[0] * g1[1]

        grad = None
        n_lines = 0
        stockPrices = sorted(stockPrices, key= lambda x: x[0])


        for i in range(1, len(stockPrices)):
            new_grad = get_grad(stockPrices[i], stockPrices[i-1])
            if not compare_grad(grad, new_grad):
                n_lines += 1
                grad = new_grad
        return n_lines