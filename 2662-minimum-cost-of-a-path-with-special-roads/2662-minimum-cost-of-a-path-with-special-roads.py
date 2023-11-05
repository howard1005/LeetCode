from heapq import heappush,heappop

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        
        d = defaultdict(list)
        
        posl = [tuple(start)]
        for x1,y1,x2,y2,c in specialRoads:
            d[(x1,y1)].append((x2,y2,c))
            posl.extend([(x1,y1),(x2,y2)])
        posl.append(tuple(target))
        
        for i in range(len(posl)):
            for j in range(i+1,len(posl)):
                x1,y1 = posl[i]
                x2,y2 = posl[j]
                d[(x1,y1)].append((x2,y2,abs(x1-x2)+abs(y1-y2)))
                d[(x2,y2)].append((x1,y1,abs(x1-x2)+abs(y1-y2)))
                
        costd = defaultdict(lambda:inf)
        costd[tuple(start)] = 0
        hq = [(0,start[0],start[1])]
        
        while hq:
            c,x,y = heappop(hq)
            if costd[(x,y)] != c:
                continue
            for nx,ny,nc in d[(x,y)]:
                if c + nc < costd[(nx,ny)]:
                    costd[(nx,ny)] = c + nc
                    heappush(hq,(c + nc,nx,ny))
        
        return costd[tuple(target)]
        