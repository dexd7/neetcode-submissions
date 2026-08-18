class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for astro in asteroids:
            while stack and stack[-1]>0 and astro<0:
                contender = stack[-1]

                if contender+astro == 0:
                    stack.pop()
                    break
                elif contender+astro < 0:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(astro)
        return stack
