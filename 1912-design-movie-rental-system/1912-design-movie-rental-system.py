from heapq import heappush,heappop

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.d = defaultdict(int)
        self.ed = {}
        self.hqd = defaultdict(list)
        self.rhq = []
        for s,m,p in entries:
            self.d[(s,m)] += 1
            self.ed[(s,m)] = p
            heappush(self.hqd[m],(p,s,m,self.d[(s,m)]))

    def _top(self,hq):
        while hq and self.d[(hq[0][1],hq[0][2])] != hq[0][3]:
            heappop(hq)
        return hq[0] if hq else None

    def _pop(self,hq):
        self._top(hq)
        return heappop(hq) if hq else None

    def search(self, movie: int) -> List[int]:
        tl = []
        retl = []
        hq = self.hqd[movie]
        self._top(hq)
        while hq and len(retl) < 5:
            p,s,m,i = self._pop(hq)
            tl.append((p,s,m,i))
            retl.append(s)
            self._top(hq)
        for t in tl:
            heappush(hq,t)
        return retl
                   

    def rent(self, shop: int, movie: int) -> None:
        self.d[(shop,movie)] += 1
        p = self.ed[(shop,movie)]
        heappush(self.rhq,(p,shop,movie,self.d[(shop,movie)]))
        

    def drop(self, shop: int, movie: int) -> None:
        self.d[(shop,movie)] += 1
        p = self.ed[(shop,movie)]
        heappush(self.hqd[movie],(p,shop,movie,self.d[(shop,movie)]))
        

    def report(self) -> List[List[int]]:
        tl = []
        retl = []
        hq = self.rhq
        self._top(hq)
        while hq and len(retl) < 5:
            p,s,m,i = self._pop(hq)
            tl.append((p,s,m,i))
            retl.append((s,m))
            self._top(hq)
        for t in tl:
            heappush(hq,t)
        return retl


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()