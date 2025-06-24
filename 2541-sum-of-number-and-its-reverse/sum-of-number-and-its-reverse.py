class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for n in range(num):
            reverse_n = int(str(n)[::-1])
            if n + reverse_n == num:
                return True
        return False