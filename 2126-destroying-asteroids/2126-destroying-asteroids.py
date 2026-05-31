class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        cum = mass
        for a in asteroids:
            if cum < a:
                return False
            cum += a
        
        return True