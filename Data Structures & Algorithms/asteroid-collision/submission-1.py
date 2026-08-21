class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1]>0 and asteroid<0:
                contender = stack[-1]
                if contender + asteroid == 0:
                    stack.pop()
                    break
                elif contender+asteroid<0:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(asteroid)
        return stack