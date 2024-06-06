class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = defaultdict(int)

        for n in hand:
            d[n] += 1
        
        for n in sorted(d.keys()):
            while d[n]:
                for i in range(groupSize):
                    nn = n+i
                    if d[nn] == 0:
                        return False
                    d[nn] -= 1

        return True