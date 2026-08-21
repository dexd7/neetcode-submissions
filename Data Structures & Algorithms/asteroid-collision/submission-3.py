class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        astroworld = []
        for astro in asteroids:
            while astroworld and astroworld[-1]>0 and astro<0:
                contender = astroworld[-1]
                if contender + astro == 0:
                    astroworld.pop()
                    break
                elif contender + astro<0:
                    astroworld.pop()
                    continue
                else:
                    break
            else:
                astroworld.append(astro)
        return astroworld
                
                        