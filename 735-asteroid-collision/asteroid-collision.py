class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
                continue

            if stack[-1] > 0 and a < 0:
                while stack and stack[-1] * a < 0:
                    b = stack.pop()
                    if abs(a) == abs(b):
                        break
                    if abs(a) > abs(b):
                        continue
                    if abs(a) < abs(b):
                        stack.append(b)
                        break
                else:
                    stack.append(a)
            else:
                stack.append(a)

        return stack

                