class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        d = defaultdict(lambda : inf)
        
        d[id] = 0
        dq = deque([(0,id)])
        while dq:
            lv,cur = dq.popleft()
            for ncur in friends[cur]:
                if d[ncur] > lv + 1:
                    d[ncur] = lv + 1
                    dq.append((lv+1,ncur))
                    
        vd = defaultdict(int)
        for i,lv in d.items():
            if lv == level:
                for v in watchedVideos[i]:
                    vd[v] += 1
        
        l = [(cnt,v) for v,cnt in vd.items()]
        l.sort()
        
        return [v for _,v in l]