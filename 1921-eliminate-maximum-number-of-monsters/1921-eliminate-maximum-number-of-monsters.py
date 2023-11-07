from math import ceil

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i,t in enumerate(sorted([ceil(d/s) for d,s in zip(dist,speed)])):
            if t<=i:
                return i
        return len(dist)